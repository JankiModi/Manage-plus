# Manage+: Society Management System 🏢

## Overview
**Manage+** is a comprehensive society management system designed to streamline community interactions and household management for both residents and committee members. The application enables organized communication, easy tracking of bills, and structured information management across the society. Developed with a modern tech stack, **Manage+** provides distinct interfaces for residents and committee members, each with tailored features and access controls.

## Technologies Used
- **Frontend**: React, Tailwind CSS
- **Backend**: Django, SQLite
- **API**: REST API connections

## Features

### User Authentication
- Residents and committee members have unique login credentials.
- Committee members require a specific password provided by the management for secure access.

### Dual Interfaces
- **Resident Interface**: Access to standard community and household features.
- **Committee Interface**: Elevated access for managing community-wide reminders, notices, and resident information.

### Navigation Categories

#### Community
- **Reminders**: Committee members can send reminders, visible to all residents. Once viewed, reminders automatically clear for that resident but remain visible for others who haven’t seen them yet.
- **Bills**: Residents can record and track personal bills with a user-friendly modal for easy data entry (bill type, amount, description, and due date).
- **Residents**: View all society members organized by apartment number, displaying family member details for each unit.
- **Daily Help**: A listing of helpers employed across the society, showing phone numbers and apartment numbers where they work, facilitating easy helper search.
- **Noticeboard**: Public notices from committee members for society-wide updates or events.

#### Household (Accessible to both Residents and Committee members)
- **Family**: View family members residing in the same apartment.
- **Helpers**: Manage daily helpers by adding, viewing, or deleting them. Collect details like helper type (maid, gardener, etc.) and contact information.
- **Pets & Vehicles**: Add and manage information about household pets and vehicles for quick reference.
- **Profile**: View personal and family details, user type, and contact information.
