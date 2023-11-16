from main import Session
from models import User

session = Session()

try:
    # Begin a transaction
    session.begin()

    # Perform database operation within the transaction
    session.query(User).delete()

    # Commit the transaction
    session.commit()
    print("All users deleted successfully")

except Exception as err:
    # Rollback the transaction if an error occurs
    session.rollback()
    print('An error occurred:', str(err))

finally:
    # Close the session
    session.close()
