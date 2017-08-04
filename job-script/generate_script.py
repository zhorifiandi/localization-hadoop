hadoop_path = "$HADOOP_HOME/bin/hadoop"
workgen_path = "/proj/ucare/arizho/SWIM/workloadSuite/WorkGen.jar"
workgen_class = "org.apache.hadoop.examples.WorkGen"
conf_path = "$HADOOP_HOME/conf/workGenKeyValue_conf.xsl"


for i in range (0,50):
	file_string = "echo Start Time of writing jar file: $(date)\n"
	file_string += hadoop_path + " jar " + workgen_path + " " + workgen_class + " -conf " + conf_path + " -r 1 inputPath-job-"+str(i)+".txt workGenOutputTest-"+str(i)+" 5.810261E-4 0.26818323 >> workGenLogs/job-"+str(i)+".txt 2>> workGenLogs/job-"+str(i)+".txt \n"
	file_string += hadoop_path + " dfs -rmr workGenOutputTest-"+str(i)+"\n"
	print(file_string, file=open("scriptsTest/run-job-"+str(i)+".sh","w"))