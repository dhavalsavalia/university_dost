#!groovy

node {

        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            
        stage 'Test'
            sh 'docker-compose -f local.yml build'

        stage 'Deploy'
            sh 'docker-compose -f local.yml up'

}