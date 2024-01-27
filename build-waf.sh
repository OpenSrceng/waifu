#!/bin/bash

TOOLS="msvs,clang_compilation_database,color_msvc,msvc_pdb,gccdeps,msvcdeps"
PRELUDE=$'\tContext.WAIFUVERSION=\'1.1.0\'\n\tsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \'waf_scripts\'))'

# a set of relatively stable tools
# TODO: make it possible to override this list
WAIFU_TOOLS="gitversion,reconfigure,msdev,fwgslib,cxx11,force_32bit,subproject,strip_on_install,sdl2,enforce_pic,pthread,compiler_optimizations"

get_waifu_tools()
{
	OLD_IFS=$IFS
	IFS=","
	retval=""
	for i in $WAIFU_TOOLS; do
		retval="$retval,$PWD/waf_scripts/$i.py"
	done
	IFS=$OLD_IFS
	echo "$retval"
}
TOOLS=$TOOLS$(get_waifu_tools)
echo "-- Building waf with waifu extensions: $TOOLS"
pushd wafsrc
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE" "--set-name=waifu"
mv waf ../waf
popd
