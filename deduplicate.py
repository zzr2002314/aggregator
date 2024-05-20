import yaml

def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    
    if 'proxies' in data:
        unique_nodes = {node['name']: node for node in data['proxies']}
        data['proxies'] = list(unique_nodes.values())

    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)

input_file = '/home/runner/work/aggregator/aggregator/aggregate/data/proxies.yaml'
output_file = '/home/runner/work/aggregator/aggregator/aggregate/data/proxies.yaml'
remove_duplicates(input_file, output_file)

print(f"去重后的文件已保存到: {output_file}")
