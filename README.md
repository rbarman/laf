An etl process using airflow on docker. (will add more buzzwords)

# Process overview ...

*  4 directories on disk:

   * /warehouse/source/ will contain source files
   		* By default there is a *claim_incr.csv*
   * /warhouse/raw/ will contain raw dataset representation of the source files
   * /warehouse/final/ will contain transformed datasets
   * /warehouse/final will contain reports off of final datasets

* The entire etl process will extract the raw claim file, create a raw *claim_incr* dataset, create final *finclmsw* and *pendw* datasets, and create a report on *finclmsw*

# DAG representation

![alt text][https://i.imgur.com/NHjZ87U.png]

* Three tasks:
	* Extract
	* Transform
	* Report
 

# Steps
* install and run Docker desktop

* git clone https://github.com/rbarman/laf

* python dags/etl.py

	* this will create the necessary warehouse directories and a sample file

* docker-compose up -d

	* this will run the docker-compose.yml and build images

* Go to localhost:8080/

* Turn *etl_dag* or manually trigger a run
		
	* etl process will start
	* files should be created in warehouse directories

![alt text][https://i.imgur.com/SYUD12t.png]

* docker-compose down


# TODOs:

* Use a service like aws instead of storing files on disk
* Create a seperate python image (?)
* Better [logging](https://github.com/Delgan/loguru)
* More dynamic process. 

# Resources
* https://github.com/puckel/docker-airflow
* https://airflow.apache.org/tutorial.html#example-pipeline-definition
* https://docs.docker.com/compose/overview/
* https://gtoonstra.github.io/etl-with-airflow/etlexample.html#run-airflow-from-docker
* https://stackoverflow.com/questions/53608780/docker-takes-a-very-long-time-to-start-macos