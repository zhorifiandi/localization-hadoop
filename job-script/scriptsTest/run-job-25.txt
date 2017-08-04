echo Start Time of writing jar file: $(date)
$HADOOP_HOME/bin/hadoop jar /proj/ucare/arizho/SWIM/workloadSuite/WorkGen.jar org.apache.hadoop.examples.WorkGen -conf $HADOOP_HOME/conf/workGenKeyValue_conf.xsl -r 1 inputPath-job-25.txt workGenOutputTest-25 5.810261E-4 0.26818323 >> workGenLogs/job-25.txt 2>> workGenLogs/job-25.txt 
$HADOOP_HOME/bin/hadoop dfs -rmr workGenOutputTest-25

