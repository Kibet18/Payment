# Business Directory Backend API

## Overview

This project is a backend API for a **Business Directory Mobile App**. The app supports:

- **Vendors**: Register businesses, subscribe to plans, and manage products and branches.
- **Admins**: Oversee operations (future feature).
- **Users**: View business listings (future feature).

The system includes:
1. **Authentication**: Secure login using JWT and role-based access.
2. **Subscription Management**: Tiered plans with product and branch limits.
3. **Payment Processing**: Integrated with Stripe for seamless payment handling.

---

## System Design

### Key Components

1. **Authentication & Authorization**:
   - **OAuth2.0/JWT** for token-based authentication.
   - Roles:
     - `vendor`: Manage businesses and subscriptions.
     - `admin`: Oversee system operations.
     - `user`: Browse listings (future feature).

2. **Subscription Management**:
   - **Plans**:
     - **Starter**: £1/month, up to 10 products.
     - **Pro**: £3/month, 11–100 products.
     - **Enterprise**: £5/month, unlimited products.
   - Additional branch cost: £1/month per branch.

3. **Payment Processing**:
   - Stripe integration for secure payment handling.
   - Logs transactions for auditing.

---

### Data Flow

#### **Authentication**
1. Users log in with email and password.
2. The system verifies credentials and returns a **JWT token**.
3. The token is included in API requests for authorization.

#### **Subscription Workflow**
1. **Create Subscription**:
   - Vendor selects a plan and submits a payment token.
   - Payment is processed via Stripe.
   - Subscription is activated, and the transaction is logged.

2. **Cancel Subscription**:
   - Marks the subscription as canceled in the database.
   - Vendor loses access to features tied to the subscription.

3. **Enforce Limits**:
   - Based on the subscription tier, the system restricts:
     - Products a business can add.
     - Number of branches.

#### **Payment Processing**
1. The API accepts a Stripe token from the frontend.
2. Processes the payment via Stripe.
3. Logs the transaction in the database for reconciliation.

---

### System Overview

#### **1. API Endpoints**

| Endpoint                     | Method | Description                                | Role Required   |
|------------------------------|--------|--------------------------------------------|-----------------|
| `/api/auth/token`            | POST   | Login and generate a JWT token.            | Public          |
| `/api/subscription/create`   | POST   | Create a new subscription.                 | Vendor          |
| `/api/subscription/my-subscriptions` | GET | View vendor's subscriptions.               | Vendor          |
| `/api/payment/webhook`       | POST   | Handle payment events from Stripe.         | Admin/System    |

---

#### **2. Database Schema**

- **`users`**: Stores user credentials and roles.
- **`businesses`**: Stores business details tied to users.
- **`subscriptions`**: Defines plans (Starter, Pro, Enterprise).
- **`payment_transactions`**: Logs all payment activities.

---

#### **3. System Flow Diagram**

```plaintext
Client
   |
   v
[API Gateway]
   |
   v
[Authentication & Role Check]
   |
   +------------------------------+
   |                              |
[Subscription Service]        [Payment Gateway]
   |                              |
   v                              v
[Database]                 [Payment Transaction Logs]
