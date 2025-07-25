// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/bounding_box.h"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/BoundingBox in the package main_controller_interfaces.
typedef struct main_controller_interfaces__msg__BoundingBox
{
  float center_x;
  float center_y;
  float width;
} main_controller_interfaces__msg__BoundingBox;

// Struct for a sequence of main_controller_interfaces__msg__BoundingBox.
typedef struct main_controller_interfaces__msg__BoundingBox__Sequence
{
  main_controller_interfaces__msg__BoundingBox * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} main_controller_interfaces__msg__BoundingBox__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
