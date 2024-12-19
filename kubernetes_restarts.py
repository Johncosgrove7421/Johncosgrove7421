import os
import subprocess
from datetime import time

# Write function to pass in all namespace and names of deployment or services then
# prints out kubectl rollout {sts or deployments (input)} -n {namespace}
# Python version Python 3.6.8
example_namespaces = ('argocd', 'jira', 'confluence')

kubernetes_resource = input(f'Which of the following services would you like to restart?\n'
      f'1: Deployments\n'
      f'2: StatefulSets\n'
      f'Enter: ')

kubernetes_resource_view = os.system("kubectl get deployment -A")
# cluster_namespace = os.system("kubectl get deployment -A --no-headers | awk '{print $1}' | sort")

#namespace_resource  = ("kubectl get deployment -A --no-headers | awk '{print $2}' | sort")
test = subprocess.run(["kubectl get deployment -A --no-headers | awk '{print $2}' | sort"],capture_output=True)


#command = 'kubectl rollout restart {kubernetes_resource} -n {cluster_namespace} {namespace_resource}' # REVIEW

print(f'\nHere is a current list of available namespaces to chose from:\n'
        '{kubernetes_resource_view}\n')

namespace = input(f'\nWhich of the following namespaces would you like to restart?\n\n'
                  f'Format for different options:\n '
                  f'1. Single Namespace: {example_namespaces[0]}\n '
                  f'2. Multi Namespace: {example_namespaces[0]}, {example_namespaces[1]}, {example_namespaces[2]}\n '
                  f'3. All Namespace: -A \n'
                  f'Enter: ')

for kubernetes in example_namespaces:
    print(f'\nRestarting {command}...')





