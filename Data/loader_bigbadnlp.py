import pandas as pd


# import page containing links to all of Seneca's letters
# get web address
def fetch_data(path):
    df = pd.read_csv(path,encoding='unicode_escape')
    df_english = df.loc[df['Lang'] =='English']

    print("original",len(df))
    print("english df",len(df_english))
    #print(df['Task'][0].split(','))

    tasks = df_english.groupby(['Task'])

    # Get different types of categories in tasks
    task_type = []
    for key, item in tasks:
        category = key.split(',')
        task_type.append(category)

    # Unique types of tasks
    flat_list = [item for sublist in task_type for item in sublist]
    category_set = list(set(flat_list))
    print(len(category_set))

    return df_english, category_set

def split_by_task(df,tasks):
    """ returns row idx for dataset beloging to specific task"""
    categories= []
    for i in range(0,len(tasks)):
        task_idx = []
        for j in range(0,len(df)):
            if df['Task'][j] == tasks[i]:
                task_idx.append(j)
        categories.append(task_idx)

    return categories

def



def main():

    path = "C:/Users/Y/Documents/PHD/GenderMeasures/GenderMeasures/Data/main_no_url.csv" # change path if not me!
    df, tasks = fetch_data(path)
    split_by_task(df,tasks)




if __name__ == "__main__":
    main()