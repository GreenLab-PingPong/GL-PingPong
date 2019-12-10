
# The impact of media quality on the energy consumption of Android streaming apps; Replication Package (Green Lab 2019-2020)

This project refers to the course assignment ``The impact of media quality on the energyconsumption of Android streaming apps`` of the 2019-2020 edition of the [Vrije Universiteit Amsterdam](https://www.vu.nl/en), [Computer Science Master Degree](https://masters.vu.nl/en/programmes/computer-science-uva/index.aspx), [Green Lab](https://studiegids.vu.nl/en/Master/2018-2019/computer-science/X_418158) course. This repository contains all information required to replicate the experimentation, described by the instructions in this README. 

## Project Goal

The goal is to analyse the effect of quality levels of streamed media on  the energy consumption from the point of view of a user in the context of Android mobile apps.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for experiment replication purpose.

### System Requirement

- Linux distribution -- Ubuntu 18.04 LTS
- Android device -- LG Nexus 5X -- Android OS v8.1.0
- Android Studio SDK
- Python v2.7
- JDK v8
- NodeJS v10
- NPM v6
- R 



### Instalation and usage


#### Running the experiment
You first require this Package.

- Android Runner: Provides the automation of the experiment execution in Android devices. Forked from [S2-group](https://github.com/S2-group/android-runner) repostiory. 

In order to run the experiment present in you need to run the script files in Android Runner from [PingPong_AndroidRunner_Scripts](https://github.com/GreenLab-PingPong/GL-PingPong/tree/master/PingPong_AndroidRunner_Scripts) for both youtube and spotify.

Before runnimg the script files you need to download the apk files from [PingPong_Subjects](https://github.com/GreenLab-PingPong/GL-PingPong/tree/master/PingPong_Subjects).

After succesfull run you can continue with Data Analysis.



####Data Analysis

After running the experiment you will get the Trepn Output in the form of csv files which you can found at 'PingPong_AndroidRunner_Scripts/youtube/output/' and 'PingPong_AndroidRunner_Scripts/spotify/output/' for youtube and spotify respectively.

Use the python script [AggregateResults.py](PingPong_R/AggregateResults.py ) which will search all the csv files and  extract  the  data  from  the  files to  calculate  the  sum  of  the  total  power  consumption  from each  run. Then the script multiplies the sum  with  the  duration of  the  run  to  obtain  the  energy  consumption which will be used to the data analysis.

The second step is to do the descriptive analysis to know the data better and check whether the data is normal or not and finally check the the hypothesis. You can use [PingPong.R](PingPong_R/PingPong.R )
file to perform all these steps.




## Authors 

- *Shubham Arora* &ndash; [ShubhamArora](https://github.com/shubhamtbc);



## Acknowledgments

For the guidance over the project and detailed feedback during the experimentation design, planning and execution, we thank:

- [Dr. Ivano Malavolta](https://research.vu.nl/en/persons/ivano-malavolta) &ndash; Lecturer for Green Lab course 2019 edition; 
- [PhD Student Eoin Grua](https://research.vu.nl/en/persons/eoin-grua) &ndash; Teacher Assitant for Green Lab course 2019 edition;

