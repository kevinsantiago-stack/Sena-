

def sumar_matrices(kevin_santiago_larrota_cuervo_m1, kevin_santiago_larrota_cuervo_m2):
    return [[kevin_santiago_larrota_cuervo_m1[i][j] + kevin_santiago_larrota_cuervo_m2[i][j] for j in range(len(kevin_santiago_larrota_cuervo_m1[0]))] for i in range(len(kevin_santiago_larrota_cuervo_m1))]

print(sumar_matrices([[1,2],[3,4]], [[5,6],[7,8]]))



def transponer_matriz(kevin_santiago_larrota_cuervo_m):
    return [[kevin_santiago_larrota_cuervo_m[j][i] for j in range(len(kevin_santiago_larrota_cuervo_m))] for i in range(len(kevin_santiago_larrota_cuervo_m[0]))]

print(transponer_matriz([[1,2,3],[4,5,6]]))