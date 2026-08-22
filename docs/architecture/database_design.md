# Database Design

## 1. Overview

The Intelligent Emergency Response System uses PostgreSQL as the primary relational database.

The database stores users, emergency requests, ambulances, hospitals and route information.

The road network used by routing algorithms such as Dijkstra and A* is treated separately as a graph data structure.

---

## 2. Entities

### Users

Stores information about people interacting with the system.

Main fields:

- id
- name
- email
- phone
- role

### Emergencies

Stores emergency requests submitted to the system.

Main fields:

- id
- user_id
- description
- latitude
- longitude
- severity
- status
- created_at

### Ambulances

Stores ambulance information and current operational state.

Main fields:

- id
- vehicle_number
- status
- latitude
- longitude
- capacity

### Hospitals

Stores hospital location and emergency capacity information.

Main fields:

- id
- name
- latitude
- longitude
- available_beds
- emergency_capacity
- status

### Routes

Stores calculated dispatch routes.

Main fields:

- id
- emergency_id
- ambulance_id
- hospital_id
- distance
- estimated_time
- algorithm
- created_at

---

## 3. Relationships

### User → Emergency

One user can create multiple emergency requests.

Relationship:

`User 1 : N Emergency`

### Emergency → Route

One emergency can have multiple calculated route records.

Relationship:

`Emergency 1 : N Route`

This allows different routing algorithms to be compared.

### Ambulance → Route

One ambulance can be associated with multiple route records over time.

Relationship:

`Ambulance 1 : N Route`

### Hospital → Route

One hospital can be associated with multiple route records.

Relationship:

`Hospital 1 : N Route`

---

## 4. DSA Integration

The relational database does not directly represent the complete road network.

The road network will be represented using a graph.

Example:

```text
A ----- B ----- C
|       |       |
D ----- E ----- F