# ============================================
# Project 1: E-Commerce Wallet System
# ============================================

# Public Variable:
# customer_name

# Protected Variable:
# _wallet_id

# Private Variables:
# __balance
# __reward_points

# Methods:
# add_money()
# purchase()
# get_balance()
# set_balance()
# get_reward_points()
# display()

# Logic:
# 1. Create a customer wallet.
# 2. Add money into wallet balance.
# 3. Balance should never become negative.
# 4. Allow purchase only if sufficient balance is available.
# 5. Deduct purchase amount from balance.
# 6. Add reward points after every successful purchase.
# 7. Reward points should not be updated directly.
# 8. Use getter method to access reward points.
# 9. Display wallet details.


# ============================================
# Project 2: Online Course Portal
# ============================================

# Public Variable:
# student_name

# Protected Variable:
# _student_id

# Private Variables:
# __course_fee
# __course_progress

# Methods:
# pay_fee()
# update_progress()
# get_progress()
# display()

# Logic:
# 1. Create student course account.
# 2. Course fee must be greater than zero.
# 3. Allow fee payment.
# 4. Progress value must be between 0 and 100.
# 5. Do not update progress before fee payment.
# 6. Update course progress after payment.
# 7. Display student course details.


# ============================================
# Project 3: Gym Membership
# ============================================

# Public Variable:
# member_name

# Protected Variable:
# _member_id

# Private Variables:
# __membership_fee
# __days_left

# Methods:
# renew_membership()
# use_one_day()
# get_days()
# display()

# Logic:
# 1. Create gym membership.
# 2. Membership fee cannot be negative.
# 3. Renew membership by adding days.
# 4. Reduce one day after every gym visit.
# 5. Membership expires when days become zero.
# 6. Display membership status.


# ============================================
# Project 4: Food Delivery App
# ============================================

# Public Variable:
# customer_name

# Protected Variable:
# _order_id

# Private Variables:
# __total_amount
# __delivery_status

# Methods:
# place_order()
# cancel_order()
# update_status()
# display()

# Logic:
# 1. Create customer order.
# 2. Order amount must be greater than zero.
# 3. Place order successfully.
# 4. Update delivery status step by step.
# 5. Cancel order only before delivery.
# 6. Order cannot be cancelled after delivery.
# 7. Display order details.


# ============================================
# Project 5: Movie Ticket Booking
# ============================================

# Public Variable:
# customer_name

# Protected Variable:
# _ticket_id

# Private Variables:
# __ticket_price
# __available_seats

# Methods:
# book_ticket()
# cancel_ticket()
# get_available_seats()
# display()

# Logic:
# 1. Create movie ticket booking system.
# 2. Ticket price cannot be negative.
# 3. Check seat availability before booking.
# 4. Reduce seats after successful booking.
# 5. Increase seats after ticket cancellation.
# 6. Display booking details.


# ============================================
# Project 6: Employee Attendance System
# ============================================

# Public Variable:
# employee_name

# Protected Variable:
# _employee_id

# Private Variables:
# __working_days
# __salary

# Methods:
# mark_attendance()
# calculate_salary()
# get_salary()
# display()

# Logic:
# 1. Create employee attendance record.
# 2. Increase working days after attendance.
# 3. Calculate salary based on working days.
# 4. Salary should not be changed directly.
# 5. Use getter method to access salary.
# 6. Display attendance report.


# ============================================
# Project 7: Digital Library
# ============================================

# Public Variable:
# book_name

# Protected Variable:
# _book_code

# Private Variables:
# __borrow_count
# __fine

# Methods:
# borrow_book()
# return_book()
# calculate_fine()
# display()

# Logic:
# 1. Create library book record.
# 2. Increase borrow count when book is borrowed.
# 3. Calculate fine for late return.
# 4. Fine cannot be negative.
# 5. Display book borrowing details.


# ============================================
# Project 8: Hospital Billing System
# ============================================

# Public Variable:
# patient_name

# Protected Variable:
# _patient_id

# Private Variables:
# __bill_amount
# __insurance_discount

# Methods:
# calculate_bill()
# apply_discount()
# get_bill()
# display()

# Logic:
# 1. Create patient billing system.
# 2. Bill amount cannot be negative.
# 3. Apply insurance discount.
# 4. Final bill should not become negative.
# 5. Use getter to access final bill.
# 6. Display billing details.


# ============================================
# Project 9: School Fee Management
# ============================================

# Public Variable:
# student_name

# Protected Variable:
# _roll_number

# Private Variables:
# __fee
# __fine

# Methods:
# pay_fee()
# add_fine()
# get_fee()
# display()

# Logic:
# 1. Create student fee record.
# 2. Fee cannot be negative.
# 3. Add fine for late payment.
# 4. Remove fine after fee payment.
# 5. Use getter method to check fee status.
# 6. Display fee details.


# ============================================
# Project 10: Online Banking System
# ============================================

# Public Variable:
# customer_name

# Protected Variable:
# _account_number

# Private Variables:
# __balance
# __transaction_history

# Methods:
# deposit()
# withdraw()
# transfer()
# view_history()
# display()

# Logic:
# 1. Create bank account.
# 2. Deposit money into account.
# 3. Withdraw money only if balance is sufficient.
# 4. Balance should never become negative.
# 5. Store every transaction in history.
# 6. Transaction history should remain private.
# 7. Access history using getter method.
# 8. Display account details.