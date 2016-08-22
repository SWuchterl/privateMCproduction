#!/bin/bash

# Define number of events
export NUMBEREVENTS=50

# Define workdir
export WORKDIR=/nfs/dust/cms/user/mharrend/trancheprivateproduction/test6

# Define gridpack location
export GRIDPACKLOC=/afs/cern.ch/work/m/mharrend/public/ttHtranche3/TTToSemiLepton_hvq_ttHtranche3.tgz

# Use crab for grid submitting, adjust crabconfig.py accordingly beforehand
#export USECRAB="True"

######### Do not change anything behind this line ###############


export STARTDIR=`pwd`
echo "Start dir was:"
echo $STARTDIR

echo "Workdir set is:"
echo $WORKDIR
mkdir -p $WORKDIR
echo "Created workdir"
cd $WORKDIR
echo "Changed into workdir"

echo "Install CMSSW in workdir"
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW_7_1_25
cd CMSSW_7_1_25/src
eval `scramv1 runtime -sh`
echo "Loaded CMSSW_7_1_25"

echo "Copy gridpack for production to workdir"
cp $GRIDPACKLOC gridpack.tgz

echo "Copy run script to workdir"
cp $STARTDIR/run_generic_tarball_cvmfs_modified.sh .

echo "Change number of events in python config to"
echo $NUMBEREVENTS
echo "Copy cmssw python config to workdir"
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/pythonLHEGEN_cfg.py > ./pythonLHEGEN_cfg.py

echo "Cloning filter to CMMSW"

git cms-addpkg PhysicsTools/JetMCAlgos
git remote add Andrej-CMS git://github.com/Andrej-CMS/cmssw.git
git fetch Andrej-CMS
git checkout --track Andrej-CMS/ttHFGenFilter_71X


echo "Scram b and start of LHEGEN production"
scram b -j 4

if [ $USECRAB = "True" ]; then
	echo "Will use crab submission, adjust crabconfig.py accordingly if problems arise"

	echo "Load crab environment, grid environment should be loaded manually in advance if necessary"
	source /cvmfs/cms.cern.ch/crab3/crab.sh

	echo "Copy crabconfig.py to workdir"
	cp $STARTDIR/crabconfig.py .

	echo "Submit crab jobs"
	crab submit crabconfig.py

	echo "Finished with crab submission, check job status manually"
else
	echo "Will do local production using cmsRun"
	cmsRun pythonLHEGEN_cfg.py
	echo "Finished local production using cmsRun"
fi
