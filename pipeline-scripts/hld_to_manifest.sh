git clone https://github.com/samiyaakhtar/container-journey.git
cd container-journey
git checkout python_scripts
cd pipeline-scripts

sudo /usr/bin/easy_install virtualenv
pip install virtualenv 
pip install --upgrade pip
python -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

commitId=$(Build.SourceVersion)
commitId=$(echo "${commitId:0:7}")
echo "python update_pipeline.py $(ACCOUNT_NAME) $(ACCOUNT_KEY) $(TABLE_NAME) $(PARTITION_KEY) hldCommitId $commitId p3 $(Build.BuildId)"
python update_pipeline.py $(ACCOUNT_NAME) $(ACCOUNT_KEY) $(TABLE_NAME) $(PARTITION_KEY) hldCommitId $commitId p3 $(Build.BuildId)
