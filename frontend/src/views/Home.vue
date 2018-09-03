<template>
  <div class="home">
    <div>
      <span>Name:</span><input type="text" v-model="name">
      <span>Description:</span><input type="text" v-model="description">
      <button @click="create_task">Add</button>
    </div>

    <div v-for="i in   tasks" :key="i.id">
      <ul>
        <li>
          <input type="checkbox" @input="update_task(i)" :checked="i.isDone">
          <strong>{{i.name}}</strong>:
          <span>{{i.description}}</span>
        </li>
      </ul>
    </div>
    <img alt="Vue logo" src="../assets/logo.1.png">
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import gql from 'graphql-tag'

const TaskQuery = gql`
  query {
    tasks {
      id
      isDone
      name
      description
    }
  }
`;

const TaskCreate = gql`mutation createTask($name:String, $description: String) {
      createTask(name: $name, description: $description) {
        task {
            id
            isDone
            name
          	description
        }
        ok
    }
 }`

const TaskUpdate = gql`mutation updateTask($id: String, $IsDone: Boolean) {
  updateTask(id: $id, IsDone: $IsDone) {
    task {
      id
      isDone
      name
      description
    }
    ok
  }
}`

export default {
  name: 'home',
  components: {
    HelloWorld
  },
   data() {
      return {
        name: '',
        description: '',
        // Initialize your apollo data
        tasks: '',
      }
  },
  apollo: {
    // Simple query that will update the 'hello' vue property
    tasks: TaskQuery,
  },
  methods: {
    async create_task() {
      const name = this.name
      const description = this.description 

      // Call to the graphql mutation
      let data = await this.$apollo.mutate({
        // Query
        mutation: TaskCreate,
        // Parameters
        variables: {
          name: name,
          description: description
        },
        update: (store, { data: { createTask } }) => {
          // Add to All tasks list
          const data = store.readQuery({ query: TaskQuery })
          data.tasks.push(createTask.task)
          store.writeQuery({ query: TaskQuery, data })
    },
    // optimisticResponse: {
    //       __typename: 'Mutation',
    //       createTask: {
    //         __typename: 'CreateTask',
    //         task: {
    //           __typename: "TaskType",
    //           id: -1,
    //           isDone: false,
    //           name: name,
    //           description: description                 
    //         },
    //         ok: false
    //       }
    // },
      })
      var t = data.data.createTask.task
      console.log('Added: ' , t)
      this.name = ''
      this.description = ''
    },
    
    async update_task(i) {
      await this.$apollo.mutate({
        mutation: TaskUpdate,
        variables: {
          id: i.id,
          IsDone: !i.isDone
        },
      })
    },
  
  }
}
</script>
