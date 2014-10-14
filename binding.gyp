{
    "targets": [
        {
            "target_name": "phidget_node",
            "sources": [
                "src/bridge.cc"
            ],
            "ldflags": [
              '-lphidget21'
            ],
            "conditions": [
                ["OS=='mac'",
                    {
                        "defines": [
                            "__MACOSX_CORE__"
                        ],
                        "xcode_settings": {
                            "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
                        },
                        "link_settings": {
                            "libraries": [
                                "Phidget21.framework"
                            ],
                        },
                        'include_dirs': [ '/Library/Frameworks/Phidget21.framework/Headers' ],
                        'libraries': [ '/Library/Frameworks/Phidget21.framework' ]
                    }
                ],
                ["OS=='win'",
                    {
                        "defines": [
                            "__WINDOWS_MM__"
                        ],
                        "link_settings": {
                            "libraries": [
                                "phidget21.lib"
                            ],
                        }
                    }
                ]
            ]
        }
    ]
}