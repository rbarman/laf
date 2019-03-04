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
1) install Docker

2) git clone https://github.com/rbarman/laf

3) python dags/etl.py

- this will create the necessary warehouse directories and a sample file

4) docker-compose up -d

- this will run the docker-compose.yml and build images

5) Go to localhost:8080/

6) Turn *etl_dag* or manually trigger a run

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