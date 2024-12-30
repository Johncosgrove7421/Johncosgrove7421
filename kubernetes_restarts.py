import os
import subprocess
from datetime import time

example_namespaces = ('argocd', 'jira', 'confluence')


def restart():

    # NAMESPACE OPTIONS
    print('\nWhich of the following namespaces would you like to restart?\n')
    list_namespace = os.system('kubectl get ns')
    namespace_option = input(f'\n\nExamples for the available options:\n '
                  f'Single Namespace: {example_namespaces[0]}\n '
     # NOT SUPPORT YET // f'Multi Namespace: {example_namespaces[0]} {example_namespaces[1]} {example_namespaces[2]}\n '
                  f'All Namespace: -A \n'
                  f'Enter: ')


    if namespace_option == "-A":
        os.system('\n\nkubectl get deploy,sts -A\n\n')
    else:
        os.system(f'\n\nkubectl get deploy,sts -n {namespace_option}\n\n')


    # K8S RESOURCE OPTIONS
    kubernetes_resource = input(f'\n\nWhich of the following services would you like to restart? [SELECT OPTION 1 or 2]\n'
        f'1: Deployments\n'
        f'2: StatefulSets\n'
        f'Enter: ')

    if kubernetes_resource == "1":
        kubernetes_resource_option = "deployment"
    elif kubernetes_resource == "2":
        kubernetes_resource_option = "statefulset"
    else:
        kubernetes_resource != "1" or kubernetes_resource != "2"
        quit("\n\nC'Mon Mannnnnnn!!!!")


    namespace = "'{print $1}'"
    cluster_resource = "'{print $2}'"
    command = f'kubectl get {kubernetes_resource_option} -n {namespace_option} -o custom-columns=NAME:.metadata.name --no-headers'


    try:
        print(f'\nPlease Wait\nRunning: {command}')
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        result_resource = result.stdout.splitlines()
   
        if not result_resource:
            print(f'\nNo {kubernetes_resource_option}s found in the namespace: {namespace_option}')
            return

        print(f'\nFound {len(result_resource)} {kubernetes_resource_option}(s) to restart:\n')
        for resource in result_resource:
            print(resource)

    
        # Confirm before restarting resources
        confirm = input('\nDo you want to restart all these resources? (yes/no): ').strip().lower()
        if confirm != 'yes':
            print('Operation canceled.')
            return

        # TESTING NEEDED: Loop through each resource and perform a rollout restart for all namespace
        if namespace_option == "-A":
           restart_command = f'kubectl rollout restart {kubernetes_resource_option} {resource} {namespace_option}'
           subprocess.run([restart_command], shell=True)

        # Loop through each resource and perform a rollout restart
        for resource in result_resource:
            restart_command = f'kubectl rollout restart {kubernetes_resource_option} {resource} -n {namespace_option}'
            subprocess.run([restart_command], shell=True)
        
    except subprocess.CalledProcessError as e:
        print(f'Error occured while executing command: {e.stderr}')

    finally:
        print('All resources have been restarted successfully.')
# Run the program
if __name__ == "__main__":
    restart()
