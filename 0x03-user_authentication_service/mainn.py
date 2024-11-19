#!/usr/bin/env python3
"""
Main file for testing the User model
"""
from user import User

if __name__ == "__main__":
    # Print the table name
    print(User.__tablename__)

    # Print column names and their types
    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
