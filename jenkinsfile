pipeline{
        agent any
        stages{
            stage('Install Docker using ansible'){
                steps{
                        sh "bash execute-ansible.sh"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "bash docker-build.sh"

                        }
        }    
}
}
