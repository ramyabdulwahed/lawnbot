// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice
#include "main_controller_interfaces/msg/detail/motor_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `op_code`
#include "rosidl_runtime_c/string_functions.h"

bool
main_controller_interfaces__msg__MotorData__init(main_controller_interfaces__msg__MotorData * msg)
{
  if (!msg) {
    return false;
  }
  // op_code
  if (!rosidl_runtime_c__String__init(&msg->op_code)) {
    main_controller_interfaces__msg__MotorData__fini(msg);
    return false;
  }
  // position
  // speed
  return true;
}

void
main_controller_interfaces__msg__MotorData__fini(main_controller_interfaces__msg__MotorData * msg)
{
  if (!msg) {
    return;
  }
  // op_code
  rosidl_runtime_c__String__fini(&msg->op_code);
  // position
  // speed
}

bool
main_controller_interfaces__msg__MotorData__are_equal(const main_controller_interfaces__msg__MotorData * lhs, const main_controller_interfaces__msg__MotorData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // op_code
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->op_code), &(rhs->op_code)))
  {
    return false;
  }
  // position
  if (lhs->position != rhs->position) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  return true;
}

bool
main_controller_interfaces__msg__MotorData__copy(
  const main_controller_interfaces__msg__MotorData * input,
  main_controller_interfaces__msg__MotorData * output)
{
  if (!input || !output) {
    return false;
  }
  // op_code
  if (!rosidl_runtime_c__String__copy(
      &(input->op_code), &(output->op_code)))
  {
    return false;
  }
  // position
  output->position = input->position;
  // speed
  output->speed = input->speed;
  return true;
}

main_controller_interfaces__msg__MotorData *
main_controller_interfaces__msg__MotorData__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  main_controller_interfaces__msg__MotorData * msg = (main_controller_interfaces__msg__MotorData *)allocator.allocate(sizeof(main_controller_interfaces__msg__MotorData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(main_controller_interfaces__msg__MotorData));
  bool success = main_controller_interfaces__msg__MotorData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
main_controller_interfaces__msg__MotorData__destroy(main_controller_interfaces__msg__MotorData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    main_controller_interfaces__msg__MotorData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
main_controller_interfaces__msg__MotorData__Sequence__init(main_controller_interfaces__msg__MotorData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  main_controller_interfaces__msg__MotorData * data = NULL;

  if (size) {
    data = (main_controller_interfaces__msg__MotorData *)allocator.zero_allocate(size, sizeof(main_controller_interfaces__msg__MotorData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = main_controller_interfaces__msg__MotorData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        main_controller_interfaces__msg__MotorData__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
main_controller_interfaces__msg__MotorData__Sequence__fini(main_controller_interfaces__msg__MotorData__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      main_controller_interfaces__msg__MotorData__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

main_controller_interfaces__msg__MotorData__Sequence *
main_controller_interfaces__msg__MotorData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  main_controller_interfaces__msg__MotorData__Sequence * array = (main_controller_interfaces__msg__MotorData__Sequence *)allocator.allocate(sizeof(main_controller_interfaces__msg__MotorData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = main_controller_interfaces__msg__MotorData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
main_controller_interfaces__msg__MotorData__Sequence__destroy(main_controller_interfaces__msg__MotorData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    main_controller_interfaces__msg__MotorData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
main_controller_interfaces__msg__MotorData__Sequence__are_equal(const main_controller_interfaces__msg__MotorData__Sequence * lhs, const main_controller_interfaces__msg__MotorData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!main_controller_interfaces__msg__MotorData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
main_controller_interfaces__msg__MotorData__Sequence__copy(
  const main_controller_interfaces__msg__MotorData__Sequence * input,
  main_controller_interfaces__msg__MotorData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(main_controller_interfaces__msg__MotorData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    main_controller_interfaces__msg__MotorData * data =
      (main_controller_interfaces__msg__MotorData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!main_controller_interfaces__msg__MotorData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          main_controller_interfaces__msg__MotorData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!main_controller_interfaces__msg__MotorData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
