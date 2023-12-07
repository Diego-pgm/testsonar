pipeline{
  agent any
  parameters{
    string(name: 'branch', defaultValue: 'master')
    choice(name: 'repo', choices: ['testsonar'])
  }
  options{
    buildDiscarder(logRotator(numToKeepStr: '4'))
  }
  environment{
    REPO = "${params.repo}"
  }

  stages{
    stage('Prepare'){
      steps{
        dir("${WORKSPACE}/source"){
          git branch: params.branch,
          url: "https://github.com/Diego-pgm/testsonar.git"
        }
      }
    }
    stage('SonarScanner'){
      steps{
        withCredentials([string(credentialsId: 'sonarcred', variable: 'sonartoken')]) {
             sh 'export "PATH=/sonar-scanner/bin:$PATH"'
	     sh '/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=testsonar -Dsonar.sources=. -Dsonar.host.url=http://0 -Dsonar.token="$sonartoken"'
        }
      }
    }
  }
}
