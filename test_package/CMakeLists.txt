cmake_minimum_required(VERSION 2.8.3)
project(test_package)

find_package(catkin REQUIRED COMPONENTS
  my_msgs
  rospy
  rospy
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES test_package
 CATKIN_DEPENDS my_msgs rospy
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

if (CATKIN_ENABLE_TESTING)
  find_package(my_msgs)
  find_package(rostest)
  add_rostest(test/test.test DEPENDENCIES ${my_msgs_EXPORTED_TARGETS})
endif()
