This document, titled **"Understanding Workday Security"** (March 2018) by Juan Lopez of Alight Solutions, provides a framework for designing and managing security configurations within the Workday ecosystem.

Below are the key insights and technical facts extracted from the document.

### **Key Insights**

*   **The Granularity Challenge:** While granting broad access to an entire organization is simple, it is often "less than ideal." The primary challenge in Workday security is managing the exceptions—ensuring specific individuals or sub-groups are excluded from certain data access.
*   **The "5 Ws" Framework for Architecture:** Effective security design should be driven by five fundamental questions:
    *   **Who:** Defining the Security Group.
    *   **What:** Identifying the Domain (the data being secured).
    *   **Where:** Identifying the Organization (the scope of the data).
    *   **When:** Executing the Role Assignment (the timing and connection of group to worker).
    *   **Why:** Establishing a business case (to avoid "security bloat").
*   **Avoid "Security Bloat":** The document warns against creating unnecessary security groups solely for the sake of customization. Excessive groups can lead to performance degradation, complicated audits, and a cluttered system. It is always preferable to leverage Workday’s existing pre-configured roles.
*   **The Necessity of Rigorous Testing:** Security configurations should never be deployed directly to production. They must be tested in **Sandbox or Implementation environments** using reports, user profiles, and business processes to verify that access matches the original design.
*   **Advanced Problem Solving via Intersection:** When standard security groups fail to meet complex needs (e.g., "allow access to all locations *except* the HR department"), **Intersection Security Groups** should be used to create precise inclusion and exclusion rules.

---

### **Key Facts**

#### **Security Components**
*   **Security Groups:** The primary way to define "Who" needs access.
    *   **Role-based (Constrained):** Access is limited to a specific organization (e.g., a specific company or location).
    *   **Unconstrained:** Access is granted across the entire system.
*   **Domains:** The "What" of security. Workday secures data at a functional level via domains (e.g., "Core Compensation" contains multiple domains like *Worker data: compensation* or *Audit: compensation overall*).
*   **Organizations:** The "Where" of security. Common types include **Supervisory Organizations, Companies, and Locations**. Workday uses hierarchies (like Location hierarchies) to allow access to flow downward.
*   **Roles:** The "When" of security. A role acts as the bridge that ties a Security Group to an Organization, which is then assigned to a specific Worker.

#### **Advanced Technical Features**
*   **Intersection Security Groups:** A specialized tool that uses two criteria to restrict access.
    *   **Included criteria:** A specific security group.
    *   **Excluded criteria:** A specific organization (e.g., a supervisory organization).
*   **Workday Updates:** Security configurations must be reviewed during Workday's two annual major updates, as new features can impact existing security models.

#### **Document Metadata**
*   **Author:** Juan Lopez, Workday Consultant.
*   **Organization:** Alight Solutions.
*   **Date:** March 2018.