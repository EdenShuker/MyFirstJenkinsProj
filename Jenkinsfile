pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        withPythonEnv('C:/Users/edens/AppData/Local/Programs/Python/Python37/python3') {
    	    // Creates the virtualenv before proceeding
	        bat 'pip install src/'
	        bat 'pip install test/'
        }
      }
    }

    stage('Test') {
      steps {
        echo 'Testing...'
        withPythonEnv('C:/Users/edens/AppData/Local/Programs/Python/Python37/python3') {
    	    // Creates the virtualenv before proceeding
	        bat 'py.test test/jenkins_proj_test/ --junit-xml=test_results.xml'
        }
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