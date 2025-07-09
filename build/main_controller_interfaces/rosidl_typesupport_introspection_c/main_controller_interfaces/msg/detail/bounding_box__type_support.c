// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "main_controller_interfaces/msg/detail/bounding_box__rosidl_typesupport_introspection_c.h"
#include "main_controller_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "main_controller_interfaces/msg/detail/bounding_box__functions.h"
#include "main_controller_interfaces/msg/detail/bounding_box__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  main_controller_interfaces__msg__BoundingBox__init(message_memory);
}

void main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_fini_function(void * message_memory)
{
  main_controller_interfaces__msg__BoundingBox__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_member_array[3] = {
  {
    "center_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces__msg__BoundingBox, center_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "center_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces__msg__BoundingBox, center_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "width",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces__msg__BoundingBox, width),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_members = {
  "main_controller_interfaces__msg",  // message namespace
  "BoundingBox",  // message name
  3,  // number of fields
  sizeof(main_controller_interfaces__msg__BoundingBox),
  false,  // has_any_key_member_
  main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_member_array,  // message members
  main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_init_function,  // function to initialize message memory (memory has to be allocated)
  main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_type_support_handle = {
  0,
  &main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_members,
  get_message_typesupport_handle_function,
  &main_controller_interfaces__msg__BoundingBox__get_type_hash,
  &main_controller_interfaces__msg__BoundingBox__get_type_description,
  &main_controller_interfaces__msg__BoundingBox__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_main_controller_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, main_controller_interfaces, msg, BoundingBox)() {
  if (!main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_type_support_handle.typesupport_identifier) {
    main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &main_controller_interfaces__msg__BoundingBox__rosidl_typesupport_introspection_c__BoundingBox_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
