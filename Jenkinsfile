pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        deleteDir()
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat(script: 'python -m pip freeze', returnStdout: true)
        bat '            python -m pip install virtualenv            virtualenv env            env/Scripts/activate.bat            python -m pip install src/            python -m pip install test/        '
      }
    }

    stage('Test') {
      steps {
        echo 'Testing...'
        bat 'py.test test/jenkins_proj_test/ --junit-xml=test_results.xml'
        junit 'test_results.xml'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying...'
      }
    }

  }
}