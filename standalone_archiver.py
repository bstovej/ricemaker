#!/usr/bin/env python3
import os
import re
import json
import shutil
import argparse
from pathlib import Path

def extract_tags(md_content):
    """Extract tags from YAML frontmatter or inline markdown tags."""
    tags = []
    
    # Match YAML frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', md_content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        
        # Try finding tags: [tag1, tag2]
        tags_line = re.search(r'^tags:\s*\[(.*?)\]', frontmatter, re.MULTILINE)
        if tags_line:
            tags.extend([t.strip() for t in tags_line.group(1).split(',') if t.strip()])
            
        # Try finding tags as list
        # tags:
        #   - tag1
        #   - tag2
        list_match = re.search(r'^tags:\s*\n((\s+-\s+.*\n?)+)', frontmatter, re.MULTILINE)
        if list_match:
            items = re.findall(r'^\s+-\s+(.*)', list_match.group(1), re.MULTILINE)
            tags.extend([t.strip() for t in items if t.strip()])
            
        # Try finding comma separated tags
        # tags: tag1, tag2
        csv_match = re.search(r'^tags:\s*([^\[\n].*)', frontmatter, re.MULTILINE)
        if csv_match and not list_match and not tags_line:
            tags.extend([t.strip() for t in csv_match.group(1).split(',') if t.strip()])

    # Match inline tags #tag1
    inline_tags = re.findall(r'(?<![\w])#([a-zA-Z0-9_/-]+)', md_content)
    tags.extend(inline_tags)
    
    # Clean up, remove quotes, empty tags, and duplicates while preserving order
    seen = set()
    result = []
    for t in tags:
        t = t.strip('\'"')
        if t and t not in seen:
            seen.add(t)
            result.append(t)
    return result

def get_best_archive_folder(tags, archive_dir):
    """
    Finds the best sub-folder in archive_dir based on tags.
    If no match found, returns a new folder name based on the primary tag.
    """
    if not tags:
        return "General"
        
    existing_subfolders = []
    if archive_dir.exists():
        existing_subfolders = [d.name for d in archive_dir.iterdir() if d.is_dir()]
    
    # 2. Try to find a match among existing sub-folders
    for tag in tags:
        tag_lower = tag.lower()
        # Direct match
        for sub in existing_subfolders:
            if tag_lower == sub.lower():
                return sub
        
        # Partial match for "domain/subject" -> "subject"
        if '/' in tag:
            subject = tag.split('/')[-1].lower()
            for sub in existing_subfolders:
                if subject == sub.lower():
                    return sub
                    
    # 3. No match found, create a new folder name based on the first tag
    primary_tag = tags[0]
    # Use "Subject" part of "Domain/Subject" if possible, otherwise use full tag
    new_folder = primary_tag.split('/')[-1] if '/' in primary_tag else primary_tag
    
    # Capitalize for aesthetics if it was all lowercase
    if new_folder.islower():
        new_folder = new_folder.title()
    elif '/' in primary_tag and new_folder == primary_tag.split('/')[-1]:
        # If it was domain/subject, and we took subject, title case it
        new_folder = new_folder.title()
        
    return new_folder

def update_note_source_path(note_path, dest_file):
    """Updates the 'source: "..."' line in the markdown note to reflect the new file location."""
    try:
        content = note_path.read_text(encoding='utf-8')
        new_content = re.sub(
            r'(^source:\s*").*?(")', 
            f'\\1{dest_file.absolute()}\\2', 
            content, 
            flags=re.MULTILINE
        )
        if content != new_content:
            note_path.write_text(new_content, encoding='utf-8')
            return True
    except Exception as e:
        print(f"Warning: Failed to update note source path {note_path.name}: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(description="Standalone Archival Script based on Markdown tags.")
    parser.add_argument('--input-dir', type=str, help='Directory containing files to move.')
    parser.add_argument('--vault-dir', type=str, help='Directory containing summary .md notes.')
    parser.add_argument('--archive-dir', type=str, help='Base directory with existing subdirectories for archiving.')
    parser.add_argument('--config', type=str, help='Path to JSON config file containing the above keys.')
    parser.add_argument('--dry-run', action='store_true', help='Preview moves without executing them.')
    
    args = parser.parse_args()

    # Load from config if provided
    config = {}
    if args.config:
        config_path = Path(args.config)
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            print(f"Error: Config file not found at {args.config}")
            return

    # Merge args and config
    input_dir_str = args.input_dir or config.get('input_dir') or config.get('input_folder')
    vault_dir_str = args.vault_dir or config.get('vault_dir') or config.get('output_folder')
    archive_dir_str = args.archive_dir or config.get('archive_dir') or config.get('archive_folder')

    if not all([input_dir_str, vault_dir_str, archive_dir_str]):
        parser.print_help()
        print("\nError: --input-dir, --vault-dir, and --archive-dir must be provided either via arguments or config file.")
        return

    input_dir = Path(input_dir_str)
    vault_dir = Path(vault_dir_str)
    archive_dir = Path(archive_dir_str)

    if not input_dir.exists():
        print(f"Error: Input directory does not exist: {input_dir}")
        return

    if not archive_dir.exists() and not args.dry_run:
        print(f"Creating base archive directory: {archive_dir}")
        archive_dir.mkdir(parents=True, exist_ok=True)

    moved_count = 0
    missing_notes_count = 0

    print(f"Scanning '{input_dir}' for files to archive...")
    
    for file_path in input_dir.iterdir():
        if file_path.is_dir() or file_path.name.startswith('.'):
            continue

        filename = file_path.name
        # Look for corresponding note. Typical format is filename + ".md" 
        note_path = vault_dir / f"{filename}.md"
        
        tags = []
        if note_path.exists():
            md_content = note_path.read_text(encoding='utf-8')
            tags = extract_tags(md_content)
        else:
            # Fallback: check if the note is just the stem (e.g. video.md instead of video.mp4.md)
            alt_note_path = vault_dir / f"{file_path.stem}.md"
            if alt_note_path.exists():
                note_path = alt_note_path
                md_content = note_path.read_text(encoding='utf-8')
                tags = extract_tags(md_content)
            else:
                missing_notes_count += 1
                tags = [] # Default to General if no tags

        subfolder_name = get_best_archive_folder(tags, archive_dir)
        target_dir = archive_dir / subfolder_name
        dest_file = target_dir / filename

        print(f"[{'DRY-RUN' if args.dry_run else 'MOVE'}] '{filename}' -> '{target_dir.name}/{filename}' (Tags: {tags})")
        
        if not args.dry_run:
            if not target_dir.exists():
                target_dir.mkdir(parents=True, exist_ok=True)
                
            try:
                shutil.move(str(file_path), str(dest_file))
                moved_count += 1
                
                # Update source path in the note
                if note_path.exists():
                    update_note_source_path(note_path, dest_file)
            except Exception as e:
                print(f"Error moving file {filename}: {e}")

    print(f"\nSummary:")
    print(f"Files moved: {moved_count}")
    print(f"Files missing notes (defaulted to General): {missing_notes_count}")

if __name__ == "__main__":
    main()
