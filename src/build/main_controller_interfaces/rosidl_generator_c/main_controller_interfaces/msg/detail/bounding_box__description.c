// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#include "main_controller_interfaces/msg/detail/bounding_box__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_main_controller_interfaces
const rosidl_type_hash_t *
main_controller_interfaces__msg__BoundingBox__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa8, 0x7a, 0x25, 0x44, 0xb7, 0xa0, 0x47, 0x6a,
      0xd8, 0xfe, 0xb1, 0x4d, 0x41, 0xc8, 0x3f, 0x57,
      0x4a, 0xe3, 0x1d, 0x8c, 0xc0, 0x06, 0xe3, 0x58,
      0x91, 0x0e, 0x4c, 0x5c, 0x48, 0xde, 0xe7, 0x05,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char main_controller_interfaces__msg__BoundingBox__TYPE_NAME[] = "main_controller_interfaces/msg/BoundingBox";

// Define type names, field names, and default values
static char main_controller_interfaces__msg__BoundingBox__FIELD_NAME__center_x[] = "center_x";
static char main_controller_interfaces__msg__BoundingBox__FIELD_NAME__center_y[] = "center_y";
static char main_controller_interfaces__msg__BoundingBox__FIELD_NAME__width[] = "width";

static rosidl_runtime_c__type_description__Field main_controller_interfaces__msg__BoundingBox__FIELDS[] = {
  {
    {main_controller_interfaces__msg__BoundingBox__FIELD_NAME__center_x, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {main_controller_interfaces__msg__BoundingBox__FIELD_NAME__center_y, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {main_controller_interfaces__msg__BoundingBox__FIELD_NAME__width, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
main_controller_interfaces__msg__BoundingBox__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {main_controller_interfaces__msg__BoundingBox__TYPE_NAME, 42, 42},
      {main_controller_interfaces__msg__BoundingBox__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float32 center_x\n"
  "float32 center_y\n"
  "float32 width";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
main_controller_interfaces__msg__BoundingBox__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {main_controller_interfaces__msg__BoundingBox__TYPE_NAME, 42, 42},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 47, 47},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
main_controller_interfaces__msg__BoundingBox__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *main_controller_interfaces__msg__BoundingBox__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
