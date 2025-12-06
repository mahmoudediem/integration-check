# This script imports both core and plugin in the same environment and tries to run them.
# The environment is set up by installing plugin and core via their requirements
# If shareddep v3 is installed, plugin import will fail at runtime.

# Import core
try:
    from chronos_core import core_app
    print("Core import succeeded:", core_app.core_run())
except Exception as e:
    print("Core error:", e)

# Import plugin
try:
    from chronos_plugin import plugin_app
    print("Plugin import succeeded:", plugin_app.plugin_run())
except Exception as e:
    print("Plugin error:", e)