// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/motor_data.h"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_H_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/MotorData in the package main_controller_interfaces.
typedef struct main_controller_interfaces__msg__MotorData
{
  int32_t left_speed;
  int32_t right_speed;
} main_controller_interfaces__msg__MotorData;

// Struct for a sequence of main_controller_interfaces__msg__MotorData.
typedef struct main_controller_interfaces__msg__MotorData__Sequence
{
  main_controller_interfaces__msg__MotorData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} main_controller_interfaces__msg__MotorData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__STRUCT_H_
