from models.user import User
from payload.response.user_dto import UserDto

class MockUser:
        def mock_user():
            users = []
            user1 = User(1,'John','Doe','oat431@email1.com','1999-11-11')
            user2 = User(2,'Jane','Doe','oat432@email1.com','1998-09-28')
            user3 = User(3,'Cat', 'Caties', 'oat433@email1.com', '2000-12-27')

            userDto1 = UserDto(user1)
            userDto2 = UserDto(user2)
            userDto3 = UserDto(user3)

            users.append(userDto1.serialize)
            users.append(userDto2.serialize)
            users.append(userDto3.serialize)
            return users
        
        def mock_raw_user():
            users = []
            user1 = User(1,'John','Doe','oat431@email1.com','1999-11-11')
            user2 = User(2,'Jane','Doe','oat432@email1.com','1998-09-28')
            user3 = User(3,'Cat', 'Caties', 'oat433@email1.com', '2000-12-27')
            users = [user1,user2,user3]
            return users

