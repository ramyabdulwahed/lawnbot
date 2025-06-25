// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice
#include "main_controller_interfaces/msg/detail/motor_data__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "main_controller_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "main_controller_interfaces/msg/detail/motor_data__struct.h"
#include "main_controller_interfaces/msg/detail/motor_data__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // op_code
#include "rosidl_runtime_c/string_functions.h"  // op_code

// forward declare type support functions


using _MotorData__ros_msg_type = main_controller_interfaces__msg__MotorData;

static bool _MotorData__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MotorData__ros_msg_type * ros_message = static_cast<const _MotorData__ros_msg_type *>(untyped_ros_message);
  // Field name: op_code
  {
    const rosidl_runtime_c__String * str = &ros_message->op_code;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: position
  {
    cdr << ros_message->position;
  }

  // Field name: speed
  {
    cdr << ros_message->speed;
  }

  return true;
}

static bool _MotorData__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MotorData__ros_msg_type * ros_message = static_cast<_MotorData__ros_msg_type *>(untyped_ros_message);
  // Field name: op_code
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->op_code.data) {
      rosidl_runtime_c__String__init(&ros_message->op_code);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->op_code,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'op_code'\n");
      return false;
    }
  }

  // Field name: position
  {
    cdr >> ros_message->position;
  }

  // Field name: speed
  {
    cdr >> ros_message->speed;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t get_serialized_size_main_controller_interfaces__msg__MotorData(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MotorData__ros_msg_type * ros_message = static_cast<const _MotorData__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name op_code
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->op_code.size + 1);
  // field.name position
  {
    size_t item_size = sizeof(ros_message->position);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name speed
  {
    size_t item_size = sizeof(ros_message->speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MotorData__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_main_controller_interfaces__msg__MotorData(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t max_serialized_size_main_controller_interfaces__msg__MotorData(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: op_code
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: position
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: speed
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = main_controller_interfaces__msg__MotorData;
    is_plain =
      (
      offsetof(DataType, speed) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _MotorData__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_main_controller_interfaces__msg__MotorData(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_MotorData = {
  "main_controller_interfaces::msg",
  "MotorData",
  _MotorData__cdr_serialize,
  _MotorData__cdr_deserialize,
  _MotorData__get_serialized_size,
  _MotorData__max_serialized_size
};

static rosidl_message_type_support_t _MotorData__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MotorData,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, main_controller_interfaces, msg, MotorData)() {
  return &_MotorData__type_support;
}

#if defined(__cplusplus)
}
#endif
