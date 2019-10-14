
//pipeline{
// properties([
//     buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '5')),
//     pipelineTriggers([cron('H H/6 * * *')]),
// ])

// stages {
//     deleteDir()

//     stage('Checkout') {
//         checkout scm
//     }

//     try{
//         stage('prepare'){
//             sh 'docker rm multiple_thread_automation_test'
//         }
//     }
//     catch(Exception e){
//         echo 'No such container: multiple_thread_automation_test'
//     }
  
//     stage('Publish') {

//         sh 'docker-compose build'
//         echo 'docker-compose build finished'
//         sh 'docker-compose up'
//         echo 'docker-compose up finished' 
//         }
// }
// post{
//     success {
//        echo 'pipeline post success'
//     }
// }
// }
pipeline {
agent any
stages {
    

    stage('Checkout') {
        steps{
            checkout scm
        }
    }

    // try{
    //     stage('prepare'){
    //        steps{
    //            sh 'docker rm multiple_thread_automation_test'} 
    //     }
    // }
    // catch(Exception e){
    //     echo 'No such container: multiple_thread_automation_test'
    // }
  
    stage('Publish') {
      steps{
        sh 'docker-compose build'
        echo 'docker-compose build finished'
        sh 'docker-compose up'
        echo 'docker-compose up finished' 
        }
    }
}
post{
    success {
       echo 'pipeline post success'
    }
}
}
