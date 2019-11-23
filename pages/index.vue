<template>
	<div>
		<div class="ui pointing menu">
			<a class="active item">
				Home
			</a>
			<a class="item">
				Messages
			</a>
			<a class="item">
				Friends
			</a>
			<div class="right menu">
				<div class="item">
				<div class="ui transparent icon input">
					<input type="text" placeholder="Search...">
					<i class="search link icon"></i>
				</div>
				</div>
			</div>
		</div>
		<div class="ui segment container">
			<h1>Handwriting Recognition</h1>
		</div>
	</div>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
