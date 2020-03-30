pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat(script: 'echo "hello" \\n pip3 install -e jenkins_proj/src/ \\n pip3 install -e jenkins_proj/test/', returnStdout: true, returnStatus: true)
      }
    }

    stage('Test') {
      steps {
        echo 'Testing...'
        bat(script: 'py,test jenkins_proj/test/jenkins_proj_test', returnStatus: true, returnStdout: true)
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying...'
      }
    }

  }
}