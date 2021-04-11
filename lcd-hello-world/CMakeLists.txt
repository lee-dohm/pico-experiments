add_executable(lcd-hello-world
        lcd-hello-world.c
        )

# Pull in our pico_stdlib which pulls in commonly used features
target_link_libraries(lcd-hello-world pico_stdlib)

# create map/bin/hex file etc.
pico_add_extra_outputs(lcd-hello-world)

# add url via pico_set_program_url
example_auto_set_url(lcd-hello-world)
