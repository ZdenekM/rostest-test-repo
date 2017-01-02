cmake_minimum_required(VERSION 2.8.3)
project(my_msgs)

find_package(catkin REQUIRED COMPONENTS message_generation)

add_message_files(
   FILES
   MyMessage.msg
)

generate_messages()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_msgs
 CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)
