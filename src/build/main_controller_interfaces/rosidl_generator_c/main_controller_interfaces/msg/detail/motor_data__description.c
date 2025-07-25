// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

#include "main_controller_interfaces/msg/detail/motor_data__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_main_controller_interfaces
const rosidl_type_hash_t *
main_controller_interfaces__msg__MotorData__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x08, 0xbb, 0x78, 0x00, 0x0b, 0x16, 0xe4, 0xd1,
      0x27, 0x46, 0xc4, 0x75, 0x2b, 0xde, 0xdb, 0xfd,
      0xac, 0x3f, 0x14, 0x70, 0x31, 0xb8, 0x75, 0xa9,
      0x20, 0xce, 0xa6, 0xb2, 0x78, 0xe8, 0x3c, 0xcb,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char main_controller_interfaces__msg__MotorData__TYPE_NAME[] = "main_controller_interfaces/msg/MotorData";

// Define type names, field names, and default values
static char main_controller_interfaces__msg__MotorData__FIELD_NAME__left_speed[] = "left_speed";
static char main_controller_interfaces__msg__MotorData__FIELD_NAME__right_speed[] = "right_speed";

static rosidl_runtime_c__type_description__Field main_controller_interfaces__msg__MotorData__FIELDS[] = {
  {
    {main_controller_interfaces__msg__MotorData__FIELD_NAME__left_speed, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {main_controller_interfaces__msg__MotorData__FIELD_NAME__right_speed, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
main_controller_interfaces__msg__MotorData__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {main_controller_interfaces__msg__MotorData__TYPE_NAME, 40, 40},
      {main_controller_interfaces__msg__MotorData__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int32 left_speed\n"
  "int32 right_speed";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
main_controller_interfaces__msg__MotorData__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {main_controller_interfaces__msg__MotorData__TYPE_NAME, 40, 40},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 35, 35},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
main_controller_interfaces__msg__MotorData__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *main_controller_interfaces__msg__MotorData__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
