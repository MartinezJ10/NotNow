<template>
  <div>
    <a class="returnLink" @click="$router.go(-1)">
      <div class="return">
        ←
      </div>
    </a>
    <div class="detailsBlock">
      <div class="header">
        <div class="title">
          <h1 :style="{ color: state.colour }">{{ state.post.title }}</h1>
          <h4>{{ state.post.category }}</h4>
          <p>{{ state.post.alt }}</p>
          <p>{{ state.post.created }}</p>
        </div>
        <div>
          <button class="btn danger" @click="deletePost(state.post)">
            Delete
          </button>
        </div>
      </div>
      <div class="body">
        <img class="img" v-lazy="state.post.image" :alt="state.post.alt" />
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "@/axios_api";
import { computed, reactive, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import swal from "sweetalert";
import format from "date-fns/format";

export default {
  name: "Detailed",
  setup() {
    const router = useRouter();
    const route = useRoute();

    const id = computed(() => route.params.id);

    const state = reactive({
      post: [],
      colour: "",
    });

    const DetailedPost = async () => {
      try {
        const resp = await getAPI.get(`/api/images/${id.value}/`);
        state.post = resp.data;

        state.post.created = format(new Date(resp.data.created), "MMM Do yyyy"); //GET THE DATE FROM DJANGO AND SIMPLIFY IT
      } catch (err) {
        console.log(err);
      }
    };

    onMounted(() => {
      DetailedPost(); //EXECUTE FUNCTION TO GET THE POST INTO THE FIELDS
      setColour();
    });

    function setColour() {
      state.colour = "#" + ((Math.random() * 0xffffff) << 0).toString(16);
    }

    function deletePost(Delid) {
      swal({
        title: "Delete Post",
        text: `Are you sure you want to delete "${Delid.title}"?`,
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((deleted) => {
        if (deleted) {
          getAPI.delete(`/api/images/${id.value}/`).then(() => {
            router.push({ name: "Gallery" });
          });
          swal("Post Deleted Succesfully", {
            buttons: false,
            timer: 1000,
            icon: "success",
          });
        }
      });
    }
    return {
      state,
      deletePost,
    };
  },
};
</script>
