suite = {
  "mxversion" : "5.34.3",
  "name" : "zippy",
  "versionConflictResolution" : "latest",
  "imports" : {
    "suites" : [
            {
               "name" : "truffle",
               "version" : "bd163128ec958b97ebc68b33ac5b4fae376a37b5",
               "urls" : [
                    {"url" : "https://github.com/graalvm/truffle", "kind" : "git"},
                ]
            },

        ],
   },

  "defaultLicense" : "BSD-2-Clause",

  "libraries" : {

    # ------------- Libraries -------------

    "JLINE09" : {
      "urls" : [
        "http://central.maven.org/maven2/jline/jline/0.9.94/jline-0.9.94.jar",
      ],
      "sha1" : "99a18e9a44834afdebc467294e1138364c207402",
    },

    "JYTHON" : {
      "path" : "lib/jython-standalone-2.7.0.jar",
      "urls" : [
        "http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar"
      ],
      "sha1" : "cdfb38bc6f8343bcf1d6accc2e1147e8e7b63b75",
    },

    "JAMM" : {
      "urls" : [
        "http://central.maven.org/maven2/com/github/stephenc/jamm/0.2.5/jamm-0.2.5.jar",
      ],
      "sha1" : "0422d3543c01df2f1d8bd1f3064adb54fb9e93f3",
    },

    "ASM" : {
      "urls" : [
        "http://lafo.ssw.uni-linz.ac.at/graal-external-deps/asm-5.0.3.jar",
        "https://search.maven.org/remotecontent?filepath=org/ow2/asm/asm/5.0.3/asm-5.0.3.jar",
      ],
      "sha1" : "dcc2193db20e19e1feca8b1240dbbc4e190824fa",
      "sourcePath" : "lib/asm-5.0.3-sources.jar",
      "sourceSha1" : "f0f24f6666c1a15c7e202e91610476bd4ce59368",
      "sourceUrls" : [
        "http://lafo.ssw.uni-linz.ac.at/graal-external-deps/asm-5.0.3-sources.jar",
        "https://search.maven.org/remotecontent?filepath=org/ow2/asm/asm/5.0.3/asm-5.0.3-sources.jar",
      ],
    },

  },

  "projects" : {

    # ------------- ZipPy -------------

    "edu.uci.python" : {
      "subDir" : "zippy",
      "sourceDirs" : ["src"],
      "dependencies" : [
                "truffle:TRUFFLE_API",
                "truffle:TRUFFLE_DSL_PROCESSOR",
                "JYTHON",
                "ASM",
                "JAMM",
                "JLINE09",
                ],
      "checkstyle" : "edu.uci.python",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle,Python",
    },

#    "edu.uci.python.profiler" : {
#      "sourceDirs" : ["src"],
#      "dependencies" : ["edu.uci.python","JYTHON"],
#      "checkstyle" : "edu.uci.python",
#      "javaCompliance" : "1.8",
#      "workingSets" : "Truffle,Python",
#    },

    "edu.uci.python.test" : {
      "subDir" : "zippy",
      "sourceDirs" : ["src"],
      "dependencies" : ["edu.uci.python","mx:JUNIT"],
      "checkstyle" : "edu.uci.python",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,Python",
    },

  },

  "licenses" : {
    "BSD-2-Clause" : {
      "name" : "FreeBSD License",
      "url" : "http://opensource.org/licenses/BSD-2-Clause",
    },
  },


  "distributions" : {
    "ZIPPY" : {
      "path" : "zippy.jar",
      "dependencies" : [
        "edu.uci.python",
      ],

      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "truffle:TRUFFLE_DSL_PROCESSOR",
        ],

      "exclude" : [
        "ASM",
        "JAMM",
        "JLINE09",
        "JYTHON",
        "mx:JUNIT",
        ],

      "sourcesPath" : "zippy.src.zip",
    },

  },
}
