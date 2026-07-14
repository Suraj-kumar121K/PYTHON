# ==========================================================
# Project: University Management System
# ==========================================================

# ==========================================================
# Inheritance Diagram
#
#                     Person
#                    /      \
#              Student     Teacher
#                 |            |
#             Graduate     Professor
#                 \          /
#            TeachingAssistant
# ==========================================================

# ==========================================================
# Inheritance Types Used
# ==========================================================

# 1. Single Inheritance
#    Person → Student

# 2. Multilevel Inheritance
#    Person → Student → Graduate

# 3. Hierarchical Inheritance
#    Person → Student
#    Person → Teacher

# 4. Multiple Inheritance
#    TeachingAssistant(Graduate, Professor)

# 5. Hybrid Inheritance
#    Hierarchical + Multilevel + Multiple

# ==========================================================
# Class Details
# ==========================================================

# ----------------------------------------------------------
# 1. Person (Parent Class)
# ----------------------------------------------------------
# Attributes:
#   - name
#   - age
#
# Method:
#   - show_person()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 2. Student (Child of Person)
# ----------------------------------------------------------
# Attributes:
#   - roll_no
#
# Method:
#   - show_student()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 3. Graduate (Child of Student)
# ----------------------------------------------------------
# Attributes:
#   - course
#
# Method:
#   - show_graduate()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 4. Teacher (Child of Person)
# ----------------------------------------------------------
# Attributes:
#   - subject
#
# Method:
#   - show_teacher()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 5. Professor (Child of Teacher)
# ----------------------------------------------------------
# Attributes:
#   - experience
#
# Method:
#   - show_professor()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 6. TeachingAssistant (Graduate, Professor)
# ----------------------------------------------------------
# Attributes:
#   - salary
#
# Method:
#   - show_ta()
# ----------------------------------------------------------


# ==========================================================
# Final Inheritance Diagram
#
#                     Person
#                    /      \
#              Student     Teacher
#                 |            |
#             Graduate     Professor
#                 \          /
#            TeachingAssistant
# ==========================================================


# ==========================================================
# Project Features
# ==========================================================

# ✔ Store Person Details
# ✔ Store Student Details
# ✔ Store Graduate Course
# ✔ Store Teacher Subject
# ✔ Store Professor Experience
# ✔ Store Teaching Assistant Salary
# ✔ Display Complete Information


# ==========================================================
# Concepts Covered
# ==========================================================

# ✔ Single Inheritance
# ✔ Multilevel Inheritance
# ✔ Hierarchical Inheritance
# ✔ Multiple Inheritance
# ✔ Hybrid Inheritance