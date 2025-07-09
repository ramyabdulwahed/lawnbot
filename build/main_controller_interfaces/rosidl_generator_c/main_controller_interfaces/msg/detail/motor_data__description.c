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
      0xe7, 0xa5, 0xc3, 0x42, 0xcc, 0xec, 0xa7, 0x0b,
      0x60, 0x98, 0x75, 0x16, 0x67, 0x87, 0xfc, 0x7d,
      0xd6, 0x74, 0x95, 0x08, 0xf3, 0x04, 0x4c, 0x7c,
      0x71, 0x68, 0xfa, 0x60, 0x6e, 0x77, 0x55, 0xa1,
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
static char main_controller_interfaces__msg__MotorData__FIELD_NAME__op_code[] = "op_code";
static char main_controller_interfaces__msg__MotorData__FIELD_NAME__position[] = "position";
static char main_controller_interfaces__msg__MotorData__FIELD_NAME__speed[] = "speed";

static rosidl_runtime_c__type_description__Field main_controller_interfaces__msg__MotorData__FIELDS[] = {
  {
    {main_controller_interfaces__msg__MotorData__FIELD_NAME__op_code, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {main_controller_interfaces__msg__MotorData__FIELD_NAME__position, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {main_controller_interfaces__msg__MotorData__FIELD_NAME__speed, 5, 5},
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
      {main_controller_interfaces__msg__MotorData__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string op_code\n"
  "int32 position\n"
  "int32 speed";

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
    {toplevel_type_raw_source, 42, 42},
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
