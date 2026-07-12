# =====================================================
# Q1. Secure ATM System
# =====================================================

# Create ATM class

# Public Variable:
# customer_name

# Protected Variable:
# _account_number

# Private Variables:
# __pin
# __balance
# __transaction_history


# Requirements:
# 1. Create account with customer name, account number, PIN and balance.
# 2. PIN ko direct class ke bahar access nahi karna hai.
# 3. Deposit aur withdraw karne se pehle PIN verify karna hai.
# 4. Maximum 3 wrong PIN attempts allow karne hain.
# 5. Har deposit aur withdrawal transaction ko private history me save karna hai.
# 6. Getter method ka use karke transaction history show karni hai.
# 7. Balance kabhi negative nahi hona chahiye.



# =====================================================
# Q2. Employee Payroll System
# =====================================================

# Create Employee class

# Public Variable:
# name

# Protected Variable:
# _employee_id

# Private Variables:
# __salary
# __bonus
# __tax


# Requirements:
# 1. Employee salary ko private variable me store karna hai.
# 2. Salary update karne ke liye setter method use karna hai.
# 3. Salary negative value accept nahi karegi.
# 4. Employee performance ke according bonus calculate karna hai.
# 5. Salary ke according tax calculate karna hai.
# 6. Final salary display karni hai.



# =====================================================
# Q3. Hospital Management System
# =====================================================

# Create Patient class

# Public Variable:
# name

# Protected Variable:
# _patient_id

# Private Variables:
# __medical_history
# __bill_amount
# __insurance


# Requirements:
# 1. Patient medical history ko private rakhna hai.
# 2. Medical history sirf doctor method ke through update hogi.
# 3. Treatment ke according bill calculate karna hai.
# 4. Insurance ke according discount apply karna hai.
# 5. Final bill negative nahi hona chahiye.
# 6. Patient ki complete report display karni hai.



# =====================================================
# Q4. Online Banking With Transaction History
# =====================================================

# Create BankAccount class

# Public Variable:
# account_holder

# Protected Variable:
# _account_number

# Private Variables:
# __balance
# __transactions


# Requirements:
# 1. Deposit transaction ko private transaction list me save karna hai.
# 2. Withdraw transaction ko save karna hai.
# 3. Transfer transaction ko save karna hai.
# 4. Transaction history ko direct access nahi karna hai.
# 5. Getter method se transaction history show karni hai.
# 6. Agar balance kam hai to insufficient balance message show karna hai.



# =====================================================
# Q5. E-Commerce Order System
# =====================================================

# Create Order class

# Public Variable:
# customer_name

# Protected Variable:
# _order_id

# Private Variables:
# __product_price
# __payment_status
# __delivery_status


# Requirements:
# 1. Product price ko private rakhna hai.
# 2. Payment complete hone ke baad hi order confirm hoga.
# 3. Delivery status update karna hai.
# 4. Delivered order cancel nahi kar sakte.
# 5. Final order summary display karni hai.



# =====================================================
# Q6. Digital Wallet System
# =====================================================

# Create Wallet class

# Public Variable:
# user_name

# Protected Variable:
# _wallet_id

# Private Variables:
# __balance
# __cashback_points


# Requirements:
# 1. Wallet me money add karne ka method banana hai.
# 2. Payment karne ka method banana hai.
# 3. Payment ke baad cashback calculate karna hai.
# 4. Balance insufficient hone par payment reject karni hai.
# 5. Cashback ko direct modify nahi karna hai.



# =====================================================
# Q7. Library Advanced System
# =====================================================

# Create LibraryMember class

# Public Variable:
# name

# Protected Variable:
# _member_id

# Private Variables:
# __borrowed_books
# __fine_amount


# Requirements:
# 1. Book issue karne ka method banana hai.
# 2. Book return karne ka method banana hai.
# 3. Borrowed books private rakhni hain.
# 4. Late return hone par fine calculate karna hai.
# 5. Fine payment update karna hai.
# 6. Member report display karni hai.



# =====================================================
# Q8. Food Delivery Application
# =====================================================

# Create FoodOrder class

# Public Variable:
# customer_name

# Protected Variable:
# _order_id

# Private Variables:
# __amount
# __order_status
# __payment_status


# Requirements:
# 1. New food order place karna hai.
# 2. Payment verify karna hai.
# 3. Order status update karna hai.
# 4. Order cancel rules implement karne hain.
# 5. Delivered order cancel nahi hona chahiye.
# 6. Complete order details show karni hain.



# =====================================================
# Q9. Vehicle Rental System
# =====================================================

# Create Vehicle class

# Public Variable:
# vehicle_name

# Protected Variable:
# _vehicle_number

# Private Variables:
# __rent
# __available_status


# Requirements:
# 1. Vehicle rent par dena hai.
# 2. Vehicle availability status update karna hai.
# 3. Total rent calculate karna hai.
# 4. Vehicle return ke baad available karna hai.
# 5. Invalid rent value accept nahi karni hai.



# =====================================================
# Q10. Password Manager System
# =====================================================

# Create PasswordManager class

# Public Variable:
# username

# Protected Variable:
# _user_id

# Private Variables:
# __password
# __login_attempts


# Requirements:
# 1. Password ko private variable me store karna hai.
# 2. Password ko getter method se direct show nahi karna hai.
# 3. Login verification method banana hai.
# 4. Wrong password attempts count karne hain.
# 5. 3 wrong attempts ke baad account lock karna hai.
# 6. Password change feature add karna hai.