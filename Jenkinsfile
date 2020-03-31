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
    	    bat """
    	        cd src
    	        python setup.py bdist_wheel
    	        """
        }
      }
    }
    stage('Test') {
      steps {
        echo 'Testing...'
        withPythonEnv('python') {
    	    bat 'pip install src/dist/jenkins_proj-1.0.0-py2-none-any.whl'
    	    bat 'pip install test/'
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