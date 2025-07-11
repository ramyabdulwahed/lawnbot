// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/motor_data.hpp"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_HPP_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__main_controller_interfaces__msg__MotorData __attribute__((deprecated))
#else
# define DEPRECATED__main_controller_interfaces__msg__MotorData __declspec(deprecated)
#endif

namespace main_controller_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MotorData_
{
  using Type = MotorData_<ContainerAllocator>;

  explicit MotorData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_speed = 0l;
      this->right_speed = 0l;
    }
  }

  explicit MotorData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_speed = 0l;
      this->right_speed = 0l;
    }
  }

  // field types and members
  using _left_speed_type =
    int32_t;
  _left_speed_type left_speed;
  using _right_speed_type =
    int32_t;
  _right_speed_type right_speed;

  // setters for named parameter idiom
  Type & set__left_speed(
    const int32_t & _arg)
  {
    this->left_speed = _arg;
    return *this;
  }
  Type & set__right_speed(
    const int32_t & _arg)
  {
    this->right_speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    main_controller_interfaces::msg::MotorData_<ContainerAllocator> *;
  using ConstRawPtr =
    const main_controller_interfaces::msg::MotorData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      main_controller_interfaces::msg::MotorData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      main_controller_interfaces::msg::MotorData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__main_controller_interfaces__msg__MotorData
    std::shared_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__main_controller_interfaces__msg__MotorData
    std::shared_ptr<main_controller_interfaces::msg::MotorData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorData_ & other) const
  {
    if (this->left_speed != other.left_speed) {
      return false;
    }
    if (this->right_speed != other.right_speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorData_

// alias to use template instance with default allocator
using MotorData =
  main_controller_interfaces::msg::MotorData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace main_controller_interfaces

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_HPP_
