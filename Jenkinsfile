pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        withPythonEnv('python') {
    	    // Creates the virtualenv before proceeding
    	    bat 'pip install wheel'
    	    bat 'python src/setup.py bdist_wheel'
	        bat 'pip install src/'
	        bat 'pip install test/'
        }
      }
    }
    stage('Test') {
      steps {
        echo 'Testing...'
        withPythonEnv('python') {
    	    // Creates the virtualenv before proceeding
    	    bat 'pip install test/'
    	    bat 'pip install src/dist/*'
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