// SPDX-License-Identifier: Apache-2.0
/**
 * Copyright 2022 Martin Schröder <info@swedishembedded.com>
 **/

#include <kernel.h>
#include <example/example.h>
#include <project_version.h>

void main(void)
{
	printk("Sample started (v%s)\n", PROJECT_VERSION_STRING);
	struct example_object _ex;

	if (example_object_init(&_ex) != 0) {
		printk("Could not initialize example object\n");
	}
};
