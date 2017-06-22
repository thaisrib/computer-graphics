import png

reader = png.Reader(filename='image.png')
w, h, pixels, metadata = reader.read_flat()

if(metadata['alpha']):
	bytesPerPixel = 4
else:
	bytesPerPixel = 3

print bytesPerPixel

for linha in range(0,h):
	for coluna in range(0,w):
		posicao = bytesPerPixel*(w*linha+coluna)
		r = pixels[posicao]
		g = pixels[posicao+1]
		b = pixels[posicao+2]
		a = pixels[posicao+3]
		if coluna < w-(w-10):
			pixels[posicao] = 255
			pixels[posicao+1] = 255
			pixels[posicao+2] = 255
		if  coluna > w-10:
			pixels[posicao] = 255
			pixels[posicao+1] = 255
			pixels[posicao+2] = 255
		if linha < h-(h-10):
			pixels[posicao] = 255
			pixels[posicao+1] = 255
			pixels[posicao+2] = 255
		if  linha > h-10:
			pixels[posicao] = 255
			pixels[posicao+1] = 255
			pixels[posicao+2] = 255		


output = open('image2.png', 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, pixels)
output.close()
