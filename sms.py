import bz2, base64
exec(bz2.decompress(base64.b64decode('QlpoOTFBWSZTWbjhR6sAm3bfgAAQQO3/5z////A////wYEs9eWz2e9993XrXWX3vudti7fGnPu++7771nfJ999dnPt3l8u+9fder33vbqy3e73sh72t81e+z2u5fdzud99efDc++30+w999773Or7rvb73zn3u9261vufN5Q923e98d5O7n2O8bXs93rd19ot93u7th6b7ffPtvtfDvpt7b33vuru2+tu9a99vrsvp3dvr3BpnuDPbT3nV959O++b1V9vp77lPXdt7rcb3m6bGzPD17rbet3vvnx9mb3enPt8ueTvZ4mvtdr3tnvTxve9vXXdhL2uF83tzvvg77ufdrXzbnl773e7lu9vb6+165tvvPfbe7CSJAJkAADQIwJkCYmmRKaeUeoEkgjIACAjU9NAEyTaBMptQgGgJEIJNNE0m1Kn+RlMwjTVPTKelP1T8qPSNPSAASakQEU8RomTTKaDYQ00FT/Up5Hio9QyAIoghDRMJkAEyZJPTFM1T8JGU81Q0ARRCCZTETTI2kw0NJiaT0alP2EknqADVdU/5f+szw9nT+nLp5/vWluvI1d5TSv4hVfxZpMz/0tIdmMIZAbmQXqSSwllL5+Tvt/nFhUviHLpy83/8X7pO4RFf/AGAVVfqqZsKCIboQRS6LAICFGqjAQ0/xhxhzh6LS98G6taVgH/Xz8CFj/pWCh/B/xT/x/t7En+fzd8TezlJbEqlnF9/psnDqkIH9EjAYLBJM2SH5bGi9VEYHJfwlFbwLzoTEeZRA2VsdMNSMA5opju/G0of0fDrxNATomgDoSZzpMDEMdKFZLPR+KboOf+VR47u/TlG2+hLQLrS3+pU38cgB4sTcNsUdcCllZABhEIyDCa+3HZcMWExBBQEQFhP82MNcZABSZiSC1AYBzBYcQYQMjBkW1gZ89xhWj/Vasmk+xEH7rkFgwo/KFhH74vNJLIF6dZCBPPb2xsMxNABf5wp/mx9aZge73/5JiJJmNWRhrReCgCdglTi5ZrGePcJsF2f/AvSLr6IUANHT7NrVUNZey9x50Rr2Cp3UJRnTieXMNuSMnxsoGB0XA9qGss37Ud5UTVyCcoPTwEbKAZjrfmuABc5qoQaGQqrKQ7AKKTCwYlmO70CpiUGM7s8B1fct00KDkbTzBdYRqNJUQVkRO7lwDuCRgfFu/DcSbLpCcpJLa0ZO1PL6c4c+H0Qd6+sc2+JhIWbmBmqkaynO5k5a86Th1vySPi/yivzzxzWgacz6CWHF9ZpSQMnGXei3wp8GDmgR4V15xWEPL39ImTLZ/9jetcLL1IJohrHaIkKROVbH5qJzeMK44AON3hHVoOnwvEfVqdnTNVmEsFDzQYAumSlaxB3l/r0OVETxKUjfZxUlFEi6yEagkXKHtZsMUpKOeLY4V6EluSGZdywZMNqK11Ku9yM9yRPjcntxc73Df0lR3oKS8NAsuBTY1LIOIJ6U1abTekunZm86fLYS64oVDNxY+vb23pXTN+AkCdAWqTF+nHKN2FY8mW0MyWXCKRl/+n5EkZAxv8r49xiXMPj25FEbe2G+xkhERZNkyEwJaPI7KUS0DHJIb3nUQKXrfnRBeufMJzfgrr3NcySMAMSB6xRBrA/FtALCpWMPnMrK0mTJgP9nq7rpy99RA9njnTgsPJq0kE/zp9tLcMCR1k7DOvMHrarWBc60CRJ3IUCNRilWNeeOWq1t/GlazRRhSBYhUkuocXz3p7vDh7dtX89tnZaJX+hKdlbNXtdvvX3tEIxQcFpz5+soG9wqevBYNA6sPtCa8IREPtM5LIOQgiSb+zT2b8IuJDy1AJHd6oYc8t2SV+a4RFciOq+2utzU3Hi8a7IMc6gSi3ePNRKJEvDoKSDoL9umyE942Dqa+UvhYIdUNAJ5Q3WgZUGDIBpOczGVIle06wmOgdI7UwuFELSS0udm2ffRHUT/7OQ46i5JmqkcUgqQlC49h6ujcLQSs34TMtPyPtOREK6INRRl8jeUo91iiRCVmSq3SBUmBGkO9jVuqhazLyuE4wFo45GlW4pzDfumQtQ+dVKJ6l/LWC2VjF12qJQgjfWwtvRw+HCQxGQNowHXpmuF3OQRNOvYQ9bk3YuGcEe+nTArXUb9L+qtkXGjDoNAUcyP7U6QolAgXoCE1DJbmM7G6/tvs32KLp8kgy7sCQCpIXjjJoJK6W3gRGJlK0eQM9LzJqaUl149OpF9uVuA4q7YwGLSJkEByfY91xESXgZn+j19/P4M/yYPhIC3+NaQsi87JDbrj37fRSa2ICQw9IkDyd24Vm0OUPAGxfjBhzNEvDFbH7Fq2agldXLVIOWplBoIk9WdkVCErBh67PK4ziFFLjU0OUEyECEBGHMhyYdxJwEnCNf5iU3JOtEbRoxRSwoELsxe31Q4nanO9nw5bsfxt7uVWAtRl6lCcYmk1xwY3B02nhoLm30MJwPtBqYYg18fqjyLuNAljI6Jfz10ugFC9Cl91VHXXGDyEUHZ2HTQvLhGU6RKqGEZqlmwyBp1WmjbBidEgUQcLm/nM6w4kD5pI2fpQUILDRYgweNCsvvwNd7k5mZuXtrXQRF8OUCSgcojM16avGghkDV1ASoGW2IiNEydF1wxDBCL4IU0n0PL6Hd5q+SsC/lxLIkjwQbhmHYkhTvl70pWR2z/j8etZO1tCYIIT7vvt4/rQB43WBEnvKnEWWVUMKCg5K1kDBkPLw0+HRPZ9Ojrw2TduE0iDWL5+KxG61ar0QDBvHVXSVBxFyRyL6QVmr6pVhdw7SCQYqKOj2OMQDsAYYcaBpUmBgv2p5EHLmdqknn/vzGaIx98JcTfSLKX06RaybZodGP5yX4xy2VX1+hWu8ZVdfH5mjdKp3FSQETbCiIQowCIAIKEVW6ir+4g7QJJI+y+LdVZm2XQL65k/pk+YRVF7hSEAULZnB0Zj3gMdUKXsARuAFXBzTFV677O9jYzu66S4IXrxZvEN1cGQEeuHo0+ZiP+pJvsHd4eMbCAlMYTxJn84PfuHJMGVg+kQKNBQBfQDLnW57d9lRTXW7v8N90Qr47nokTwxyztbiAc4GiGxY7OhQaHnu0JmyLBvZHo5lIaFtKh3zNnZAO0EEbK0oDdjXT1elNB33qm30I74mHft36iOjaJs5TpRl3FEmOTlBJFhVzNvI5LQGscO27dr3DWltAjTByawtqohKhtaUFbApSw5JU9VDYrsI6rjAEzOhVTStEJeW31o1dX5cL379e+NxSf8QI2hodvkUSthJTpFoM3zKAQTWApwT6lyMiNXHkdhj7aBsqXycap9ufvv4bVaZ2UWvHE709DSMR599PkUaIRkPfq6bQ6Il4ZMHHA5J5fDeE11P4VAytsTZeGCEQjJAEgqLCBVUBcghKWMUNzX9qufOtcavh3V5U5TH4LFVYiJIvljuXd3V59XWr3Y9r+FIuIVt0zMMMy2ug9xkwwgRkZjMg/Rv8M0dfIm96B2olDx8hv4ijFvS9kNAZTpxvUz4IAXogYdgCYgQkWAUHkVhQdEKmTLy2Qc3CHIGGopjNtUirgrXCjelEVIW7dTVndvN1cW4PAXQTlCPwhAMfHxvx+txxd3Fi/tl3x4h3XOPTz948odSS6kJsYNb1mMsd7m3ufTtooARxqhaIWNFQ45mI5cC607YqjOWNU1AJxVal8Ae2vHBFdAXRCeqcK381qogktBKP1Yj5V9mdc4CvaEG37P8KEIyyep+VUkikxChturvV3fHZr2fTamgGPiHDjSkm7zHB8w4s5E4l4GR4JI9G+mPJ3CL0PjS8G9Kpq0d/BlKMqUGQa8FrFvwQ36zJP2Amf2+cqc6zUJak2MkKkutUVFVNMRDVwFmPJZX9mao9M8ZpCRZRswzcgwkkH0+H8jRc/Xp+1y31eJ4KCgfXQjZC6tFZgaiwxgJD24QPWTMkGZsPFkBkhSUnIhBF1qkKiAHKFeRoAzMHpoODzevX5ClRJA7OHLA4JJ3zdqclHHDRPpfk2nbNXtqUymmLvdQIQ2IdKL4q0AaAI7ADlTujmLChYUgVSAGnpPGm3GHHok3iw8JViYkGD1qKJWETbnvioh2n+gg+TQ93E9wbfseyZiDzl2dVwJ+wYYIQawIyDCoSjAyohMYCE/Dsk6K9KAZYsiJ4d/pb4Oh/HbYgkcarXigzMKrVBwu7f1XFL0ZoaPGLgSt6Z5ezf2vCXBYhA9e2Hn7/im39nnP9LVTJTtdWanRhbf5jS882l/AA4BYRH3VhGGYSIHvuR/WfEYxNaYpbIXKFYF0aFdCGIOHz5r/n88+i+mGPDvvysCtLlBRElRAihKhTQcLGKg2kD9Kn6fa2rex7ryTEumkREHcL2FNs9XREHkeIp7dARZF+ruL89cEHDGsdIUa7ZlShNd8lrIEyUog1TT6U/f6fKE9Mh6ThaElkZBUFUVLQlEqQVQkioyCwBQDwlVBSSMkL/OpYQBEYsBCJFSSRZBYsBVBBQUiwI+HCev7/z6OQAMcTlv6rhVnUyjK0SmNMiwy+QOg9y7aD1XrINIbun750qm0bxu2U9yzHGRMbUVUdhBJVEYofLzefrctdvXr45PifFZEdKMDsoZUeSWzLWEqIIgtJa0Oyd/Vr6zwvNgVHCcqSoQHVECwcC0AQWZ/l4IOkzjWygLohQBMXuBWVOBWVMTPFBG80KaKgYxzeg0TLRcFBcR4cL1i3cyxGrOGJbrCnivb6ydrYwlrcV2psu4lBQuNAKc3YOJloY5t04EuMJSAcSKgCjJIONGRMkIRkSEQWb9ydg3RPsf+m7y/etVfEgOKQE0ryibnVBddmf1dYUPF+1CZ4uUr5JEtuH1gn3wLkS5ZHEG+jL5IFkI8V9Xfp1gwR7iIKtIa31AY/hQPIgW1KheebITUMulSaxWO5ss6IHhVl2wQGCyWO4ot4G2XCoT+K3VqwkWAbHg98wVtIlbtJImhcZQV6wg6MTLjhzW6WRMYrG4N3zCDaWhOz5tuzrJPIX2Als35CRJHLgsQlnNOk01HFr/TGUv3wh0iGBqNTe/AZ4kRVDOaCHXIB43N0MRx5Th7NBnke/grIO9SZ6tFTi5oXgFk7fI+MSOggABWqTi1lUyQt+Y4+INAjn3cpev4O1DDiRkV/Gc1sLXOBcPpYMSC+9pwJWpT5eakhaEp3J3uSTnr+qOt4u87jMYByuheqSWoShD2TXOj3UsaKIpclvZN33EPkMbvlgPBYLT42fMFlcyZQahUAiGEmbK+HAj6Zg3nfyQw7EZTKcypCwFjbgFENTQHdCB3/K269KLI2SH/AFrTysOHHSNhVnLfloUFN3FzKJINknd/4KvxLx2ld3xVBm2lpIgVNJPYqpPaLmnTYssyOx67J5rGqaKW703WTPLB7Od6EGm3s+Ybc80LcySOKBonAoBIV6nfIMGVyKbYvRe64V9Nau6lrkd2OBvc2IMZz18Q7pV+fjs28NvTfHZDq1TXrX2EiRMKoG6FpD3UZ3Lx8b9nL44y4pr9ZUtmVLkp+U/VZWaDP6lrzcIvD6jglFKr0auxLN6ZFyvg8GBwTKqplEyWdFsyvH+6MNu4cpjLr/H6r9Ovj7NeRGer3wI5fAzTLM/X9Hdz17n3cg6LC3lL1fO6cn0R6rnA/DCyQp1gwOJffzCJfT612RDcCRQHz8SGcxfRHnDlPDTFgFfQWE91GBBCisAoOCECpVU9GPKAkPzZDrQ2m32iIG4iCuTHShLW3USioP03e1mGCNBCYwgnQXA91mXTCqlIg6oG74af9wwylKNhN+GSwoTLJK43FohKAlnaGiRLf62uEyM/eV/l7MoC0Y7M/j1j2a/emvi2vLDjeEvVZrSR5ITCxJi16W0foL/hxik2MLPaiOfXzZN4l+ILNg1FQSQH8g+6DskoyZEGPxeEhckpa92rDurSKTEwypGInSHVBFdVb5K+ItvJD0AepFsi9HLn07TUm33e+dvd9uBvUcOWAg2OIMNpRCz7akLWGr2oGCbkCjzlaQuiEWoif05xl/LRhQRxbdpfCym3QuIIo2fN1u22kuErIKQKQEkZMhEKJyy4K2Xv9vWrsAfgVz4bQA2LzUd27KhjL3XVFI4tnDFE+9DssiFbHEYJSGIIhmZEecd7QHjdEQJCAUQPrAqCqkIiBhVCIK9QCYgR+d35QHMOuODyoH8q7YsXj0AXpj8mAicrlaKSIgknJBaI1Sh/JRx64YvQmZQ6jrxxil0JE4rUSH8DDKIBAFJl/PT3CmcWFLqMjaG4iksIyZc6HVRSkB6E6wDpgkwQ7MSTtYbBffhWMxQvJV+Z4oZgMKngijXvorpqQ4oYa6QZIG+VbbutUjZw6dA3CEsxcDHAk2kSvbzooGw5WPviGLKNJqEApF8F3i8tmtZUlSmTDMMkzI1GVj7a1lefftxDEkrjJwIpYPI9fBLKkmKvPeSev1JTonEqTQVYzDC6JTTJS2GIBWABaonOe7vL9/khbGJn7Ou8x1oxuqXaCgOkQubqudDQXxtVoCBKa/QJ1dX6uvRT3iDAUGZhskl2/jlyPzzrH2nym+ho+/ZVOPO1JO4u+leAhC2PZbtzkt4OJzvshX+9thZObLqtyh3Rj0pSA3SEykQfKSk8ljxGLyZyWKz9R3dovxhxoGN9N9p9W873J7DdaPnXLuuORIey59110Yjh+1p6z+/ZNzkPcZC3sj8sBVNVDnRZLxXqNYCvrUEYmZADwxFQp4m3yOcKXC3QAF8pMkreP5hPkohvkiE8vZkYEzoMxZZKFsEbDaU7qDdQHMWrClizUGJumjRkiNint6/y9ukp37vryCUUBraerDjaseKBHy2/jNaynUwamzg4oHMIawZyjJAZoAXgGIQIIVqmR0HV7e42o5o86FFeEWlU8Yqm+QtUO/hKC7uBBI+V9UH4o11YfLjr3ePu+Ba1/cUpCk5Y/dFB0e1IEh0sgKeXdQXhGI3DjUko8xCiXvBzQxq0kEjTFkTieR1nHRCKEPRqRB2ydDXhYctFstVSqCB4ma44gGGfk1lwS2+mT0P9Mh6R7LYmo81PkY5fC82hgZqhdu0cNK9EEj3iH6UdaIXdRUNeXVnoM65RZQtmVs2R1bG1+d3kYSYsKMym/yfZHBPjGnW91DVfjZ8XmU2xs4WkGParZiAdotzRrKDZuQ48uAsesvz9CvWaXv0jMfhgwYt3JeMaFKZSZHrMz3Z5I/BYLxflPPOesQl7pGwDUdjaH7BTyT0s5DkMU7EsbfTOCWacMWB93mTj2pn9+zUrrvzkDMMMnGCQfoFbkSkfa2/7xnkJNy8aeH6w70fVD6AhiPMjnpfH+VT0OdbjEcZiUv6bVC9TJlsIWi3Z578np0bZZmUjlBdmNejasIU/EFDAM+YuHxdP3ZswOx+IEuASp23Jp8FkR3d6QeBSzyGrH9c6dgwl/fbLfTjY+DxL2CiBBGAhmGIFtc+CPiCvWvl+EeLmPHfyafau22fMA8+Ez7FOQkTqHNU9ITvlM4RKgtmgavLjV2ckwqZEuArgqxMzGvnFx8BKxIOePjSbzLYJdGm9Nda+tRMQGPXdgWXwabTBM9xX7t8sPUa+8KU7ynkocKSwxAkgUf122UxR1iqApOyFbJA9FGfroMaKYf08MKbWTOsfUlezWZo60CVDONgDDEMI8exHbr4iwLkXqECnwybtXNqiRiysp1lD6UQskwmZ+TO3BllGqA44OIjHx69O9EQK8eFAe+ECJfy0TyFzvpoLJq9fuGKFPPFgLYljbpdZXUCwwnojkDQgmoWMmgG1xpsIecdFQ7yXFSyyctebRbuxuC3q5bnThx1pmgB6NOroIqeGvw5hfAWBdVvngYGkMeW/hMKoAopJna7bhfwIyNC7LakMvWtfKG7YRKISteeFYeV7GpkkySmy4KEjIC8tyw6ODA7DMMmTT2rDUhvxeOybTh6lz7xXVVtcMIWq4O5BhiCktcdd+1klYfVB5nhCYFS+9or2WQ4Wup42714Q3VgTsjSyQiTlGkQH0glIlfmdZ8OMoXj9hC+QemwbKqc/aJiXMqSGQ5kOOlKQe8Ix07UPZUD3QgWB4oZFJ8z094e15SCXlsk8KpZ5qedSFSJSIQgJ40Ust2/B7d3e65+z59nZpb7Qc+VyRNmSr4qzltSZC0qUhgRWLLe8TePycvRnTjouTruC+Rf5lxTPwur7InV0o8Ki4QiAkqAlONTrb1ASprQtj5TIW1oJ4At+WkoLEAIFYBoDAo0EYVAJSMhKZBgwCCrCDVFQQiymhJESSwRgEs5pdiIQsyX0qXu3dLhewkJnybKNpJkVoFbbVloqqJp5+3owz457/vz0oR7M6Ib4OSjogprNkNYPehyrWEqyOeytFQMF7fida8r2vFSkSkfRyOk4HRDREtdBpYoY11fgN3pGVZhdsaaYaREzJ5ulTqUnhQlYaFqHXUKUD133ODzxs2yNlhA7oALUu50BjShBB8EKvKMuJfLPEzF3qQhjSkckJQ+/gAx0AQREOOsG9NZjnfNaspE9VmvLwBcZADNNJQUwYisgXYIknNcsAsdGQUMExg/COxy/f1svKfBEJFgliI105tawtpM5tdGSyaMoJOblyrJJ7mJUw8A4/a3tHPq7VdAyXyhofLmmpyR3qBbRLcoO4KyBLyypAYipCLEIxhFkgjAkVFBQkRAEiySKIoxEYikgwAFiCgkjEIqwFPbsygTLCmsmqB4jVSRQXVAgI8jUJgIKxV4zN1ZxUsUgiIClyrDIpAMBaLw0Ut2FKDApgDWRMhHf4PD5ANJlRUXxAYQBQn2X91PP00bTNz9yg19aS2gG0I0sFMI8GDRQiUsZSomn14bKeXEhMgySVIIgZUMlAy/EcvyN7TbFihIdc4NE57e2RcQUJihOtAnouNNFQlDCkkTxkCwkBq1w4KCgDGqxTcIiAEDbYWYlWCMEMIFlQgeatDw7MBqHMiGSEKBhBp0CyLVCT1aIe95WIFwRIOIpy/TX+vOuDC2hLd44pvbHkPPX48uuj8RyaIOROpHZon1xJHtDE7szMfVpgHCEZJCgnlVJIyRlmsdD5s1fQjdHOAcCDEIGay/SBSqOyXqBuL/ihMCMWIr45+gDfRL6cPf5V8Zz5Z8dPqwMEMGYU7YqzZJA496lAPytEwCaN+/LYnk26plEsEJLyBS9CcgWIS/LAXFXbKsqGZ4qBfOsXwRfAAAhWEaQi/QoAyKwAj545RB8g+skj49OlQDthWELyxFAHkom6p6i6WC/+rfb6dNKT+35Ip0ZR5ToQagDCNmV7XoPeXudElxDv4ffaVF8IrAPMfqG6NeY2qAwLXt7fPDwV7eGKSzVvxxfBddFOdb08GEnsR9de74wF+gWuUjdsNI3vu2t8WDXc4t+tiCaUaLB6OLqmfkztZFxSKZNCmzge9X7RJ+6O8MCsadzedqtMU3BlYbIMhgYLDWlOG1DINCPSSZ5gMSKz36ADGOiRO179RQiIsTD47kEw5bgtHtemvl/Wi+k+aG9jSSDKHiZ9Nunxt/oQ1uc9gI8ma5jFy2KumvMBfWvaIUEwbkldDuigG5fL8eTbId00ST+lnTOKeAqaY4KhkpAZUQ8YkTz3M9p41jYBdiYSUXxiu/Rpre8Lca0GGwbhea2M+dr47ZII0YyBEcyMcMK00Is9hfPe6YVfx53QZQNB0g5OzfQU1T1ANRBOt7njOT+bhHHzPSe1uMI2nX2Trt4OLwygplDrDkYDT/WaogDhnEoseF25PpUz6eOsIXRG6JSiN23MYZYfN2yTxugL7WEpEC72F0YiElAWAJvRe0ia+JrTAJ+fYdP9Ekvn1TlvG6VK2Ks022t9Ju4NTEBqUiZITBraQlNrAzhIWb6Mq00kLQxDSlhm1IPcD4MViGIuWcpRJdZLUikygxAEocjBSoaT4/a+rVIOLLcYSOvly36itnkSSEHI1NwNFqhVJvmaGchK0KfGAYTpf9usgNcriSc9z0suJfd5IQ/H41iU4NEWotnLKwahj/GJ+FcvU8AHPTw1+W60UUnODyEhgggkFIUc9OVixB59qbfVKD9Jhbg5ipOBEoClYoJapoGz9q4RYEly9Q8MrFLTDoe2TAgZNOJs1sQoFtnI7QwAChyB6wAOFMPCONDdWHHWNAu3K3eyMmxWJW8xqgNUcdaEQATKbBOR+Vig/b6SLJWWqQWDUKrMdhJEaChpFkKLt7aBXXvVwFKVCRGWFZuQOTvLeyjEA7DMzMtvz2v+/13glSa7LE+7NmIeG+CDgQAI/1i/0hMBm4N0jwN5dLh4fG8X9QHRXM50x7BdfPTVjUUprKHJ9o0szASRfOFHBKGdXOvJ6XPFjjoFqF0bxGIEEJjIoObxLLqag4i4Bl7VQf7YFpvgyjPcSqvlCK/iE6JCgCZOf52LAf6OjPACJIQFUIgknuQCTyiWViyDEkVEum5kk0fNNyYjBVAN7bZVxAFH1wwzjvP9xCTRZ8WmKpmYBPUE+/6ExNLFTQyPre+sZqjMVJzSVC3uhxj+tI0QuZ6Kf2WUlVghWWiFI+4Phkg13IXI0qUMKhayXXOAyi8Jgvee2eR3IIlKrpjQr1iCaIxeYOyL8MTF9VqwpFiFCeM0FUqS+NVwLmCorr3vr5OqDHH1g+6l6hoyuvvRtmYZTkNak1YS9IZNn9Wx0v246zJMWVOei01ygrCTnh7oLhbrfp08Z5PuueFs6G3NTIelYfq3HfLIU8/BJEmm1Neb3nX7Q1EcSAqYx2vcgOzn3f6skW+oSmQpprZVS1NWoqEswllvasunXAODJNwsr9R22sZ65jsf1uCRuoxdoFJ+1IBIAPAQT8CtmU1QucF67fLFDKuGze0txAVVmbkI66Cm6sfwg1S5VudvpdTr5kbcYLVENu33IJENPhF3bDB0gJTMhb4+EWwFcAT3sWiRM0rJznOu1fKFnD0llOjeJEnsYXYpJDj7OSXBmpZgatNsUC9L+3GS1qV4D4HpDcZKxCLF/5VTLQFYmZmGGNZLyLvRA7kw+gx9OYb+mNCJ1uR2Aq5BzlTiz3rIai/aY69Hfetw5Sn3z+cZeNkCsUiCDVS2cWsB+3j1UG18CXAjlw0cwbFFIjZyEXbHG59zTehKXkkw1DPhv2Y1XuvEqMdCFnXzyyH6yaQ0b3FlNH2kT257uDx6rRrUpCN/HGhXQdtucrqqVGCIYhB+2OPE8FGkq75004ZK5BEeqpASJFERfxUhKJEVSKgAIwkUhvvQQorpRf0rz3KlI1agny+3LfWCfZuo1iO0U6dbyRcqnVqNNdUc6fO3T/R0A0gesOwVX08HXXmaDj0pv1M9ZqnuS7AzYIV7MCWC1ZTKg7/OItyO4+9ZVmpIiJRDPfeOc7/KDkpG5aKPSH664vPnZ7Z1OGxMfzhngfPiJLlclY33ZzL0d/nVnAtPbjszCOC+qUKkIotViEcSMzehrxshNcoM1FQ7QZFJ83strfQHakqQfgVKQAGMgyCQH1Y2ALLIlt42zF2vBXvW9AWaIQCZkR8S8dBKND2+RJeulWEBj53VMPsh/GJinvLpCZBr3dVCT4BJgQ3TjDIGYBxemAqpIrpEuR3LgGUv5dMc/3flVG3Yakg5z/E01SVWVgFmzDIO9E7DnkkJHjDyjSXrRkmJYn6RZWivGDNlLIwR5NoAgI0dZIJezuIPWbJCgg7tQw8MTECFt3HeEC5ANUUCK7hZJRkuoktWumL7+GylY2aJRzaZB4wY4GGVZXMHDhRkIhdM/r4sq1TSxbijGnfBwwWQyS6CgCfco0xlrgbokQrCEGCg4BCB2RB2/uoUTrqhtaIPKBKQjeAcJcjSgv3+z6d1Pi+iVz8ZJzTUzt90ZpLJIG1vNHTQ3aQksNiOkBzurr1xmEizScgpJTzqrineK/LNzyzm5CpD2Oell3+DlAQa4sC/frpUE2dFSDRh+jTDA1WBFUPvLOpsc5XvQacPXHq0QItFXG4RM63lLZ0oYCdopqBTLL4bwt+iMs+X+EeTto3KiWkNaNr4ie09dCTNGJbV+X2BUZXwHt71KuLhJIrZJBnYQhyBynR6bdCFmODWNN4MWZGXN43b1l9PHLsatv7MLNmqvLSQQW1ROBJY7UoCbgvpBGa7elgOVE7KDFqxNfYAz4nuSvpD9Z74l9JN+nytQTBGnh1qxvb+wbYP8x4HO45nhCpzJvt1xOp6N8qsedYJn7J0SY5W2a0IjKmhivvv23dEkvDb3VGWDDyd0Cy6QA4cvhnbzP3YFpsqeZ7HBeMVDVfqniD29LUWQcUg/bYluq0lDUzGEqnPR1yOGEWr5VbJ6uhZlXtRcK9/0n/HU8qb8pK5UX5RGq1EnLNoEXlwSoj1/fDtEl6WynFhAjabBuSQdMIiRd/j4aVOSFJx/L51IWtLKJCiA4ymufVovwfKjP0pVN7RYCoxsmK/nTbideTxl8PeSu7bfYwe1cMDZRiveg0rMUbYWPQyEwili/+KXD5w7u+T4mqKofohYg2c8T/NubVU4U7dYngUlFt26TlbCHsPDmC2O5UzMEdwrxyvyUi9PChJHGJK47vfMCJGlR4K31zMYU9yp/jVzcbTu4Yoj+QrYWCsDfHkj2ocNAwUbgBx9MxHc1UQkb6e59H1b4lOEMfBBNv/eEsvr7qNfEP5Wg9tpfMFM9fLNtqfRJpnrQnUTepFEhMhd0uL2szFG3PDT56TRxQCQAd2Drrt5y7ayXMxk3QsYtvcDbW4eGHn3uN8pCyuJ0YEnCeH7+OD+v8iHH+4FtoogvwyGca1ShICpmz2X20ure0HJUpBkp8+JBmQLWwRQr2dmKY36nMHNfTWXhYIop1Q/yD+iNgJeVw371nsT2sg4ZK9nZtM72AmATkabSdfmDa+g2a3U67wOO0mBJ/sSV1aPQTsTS47d0FBay0CZ5JWP6ehISParhL4jCc4xiW/XZ30QwBTgsYdRrYSN66cLs8ZNHP3+nielbxEC/1oD2LtugWof5ymn5SjzzHtaJY2O6VaErf38GbNmepUwwuXLFN/fNhgzkLxCG1r8WJ4YXqUIkgx6jHKVivZ7H5tVA25SalaSMM1t2+HeTkOgedT8ZEaewJuohgZgBYyYZm2tpT8TiO60mGcbufqj+qHYIF2/l0vHkFdP7vuMEf1ej/f2G2UIfj8K1EzO7m69DvEHETl/9o+TmDAkQMbIUs0Sc/88SFdIB59P4+nrvgXnywYxV+5IDlffvwvn/HhpCBfAvOwqf2Lvl0UmeD76VJjNGXpBW0N4QuwrqgAPaiQtJavb3bfLPdqV06Lhz7M1s+2rZReceeJfNmeioqqu540FR+1rFuvz7Y6fUc1CMyQT1E9dbL/f79cCRfZNskTMhQ0MZdcmGwfN+WN3mhcd84iJAsTDxZ7uFRSiEKIj+Xc8zn4Dsxnn7iQOtAGQM3rCx+W6AXP6lzJSp9mYe3r652iypEB0mEJggngyOsQRDNtr/ebPWe2k4k9tEuk6Ux65gy5HeCSi17aZOlcx22glMwlIIwQhEhWiRXBF1a1eT/H/G/XH3CsH876zs+Os54SYYJhe9jVwQ6/KlGNOIlZ457TYzW/agbEjTEA3IVRcOfMRGTSD8xWvty/vZ0IHqHf8LfbwuwSkJO3Cj043tqVYITk+XK8PMpPZSSNNJfOtospEg9CngjQGvIGJBMakgWxpQtDhDVZUmZsSWLMvalmCVG6VVV4SBR4mPx08NLYmNiTzsdvaK3Zhw98nLozx2Nugg4fp2vh57MomEDxV57U+S6T5Xyz9mE9/XolQmmGR38pXgwx70iiKv5Yp8fxuQzOZRTe69eFg1IwYRO30e0HdcgVv1nrCwisQ7hPI/Ls3VJUtAlRokhLHYUASW9Da5cX2X/f8H5toFzHkDYxmm29pY/Z7I42UM4GyA71dSt6wZRqDgGWHKi6YPjgE0KZ6hzpKQvKyUzDs1LtRm65u8PO5/zu8jhurEatiC2oJKoWFfK9FagGxH1psDEg/vXst5qY/ilRVhhCFK50BOfSKbbkXyPnTEfxMl1cof7aGnj9ZuThE+yJQwFSM0cKa/CPGqHNXnspgPahC3TEHBBH5JJFYlHXuxyNWUepjKJjL+gL3iUV9+jOuv+xqgTIDu2XEjf7SU2XmNauOCyLAH0fTWVZ55QZhy2xOWP2qvRZsw0OdiXP+hIe74ukl8E+4TRsy9oLMQvuFYsqqauGLvMGK3OdJ68BFQXfW4Hozd+MX3Vhs9VM8h/i7jup+OyMoMzdCsX9gLvQG8t7D47acn72kbR8/mFQyBSojZAaSLbuy3PX/Gbg18w7nLe7nbBpu6mojzluTt9XGgXQCdk3J6Sheu8MvHm0qDv/hjrmvlLJIssInkjqle1wHjxpu1Zf/TQMbjpQD0NBGHsgd2HrSpKnN5kJPJDD/LwbcQjgly7RUoNBqeo2szOI7al7V9kQ6qpCTRCyDwqoqeFtXUi6P/MfZDAR5S4Ap2EXM22jbNY7sf9h5q6I/7nr76qmsWEEPUXiQlO4BgQQYhRwqi/vBEEEPX8lMMRf4F3UHZ8qfns1XR8YS3YBYla3E8MgS9+GgC1/bcOmwS2JLcJVCWOV/8Hm19tr0wF3pKjSpaVVLkICUdmUq/D5GgD75t6GBV17/dR1JrvFoAcHviJ9advH7IAfs7GaPXlSRpjjbiwXlnr1UoNCEwKjRulfuaLSgf298sjTN3E34hSxq3b2m3lpBZubaKTKgw58jp3z54adP0yDTatIJdTuvR3TcA7kl7QvhIYEwZzxm9aIjCcp65o37r6jYRB7SMKeg2dGqOvuLivKFb+wJSF+76JVgS5aKSFcem45dSriXjFEIg1kKoqQZZS0UMUxjQKTM0/F56/h0U2MLjdXnc83QHBiMdMkdx77OBWJF9NAXbwpg9Bvbq/E5hUzMj4tspsuS70MsC2NVmZzwJyKV8PwezylU6UaeqdePRygTRKFPhxw6MlGJBNMaFGekwkrlxh0BZFYf03MO9FdTo00g3PG/jatNk6lACEYh4V8/LaLyQZBJ/1/Xb9ppwih9a9aEUIZQkWFW8DPWi92fTvJTpgYyQMktLYf5LG9PS9yEpCXLH3o7dvtQwC9XFdqSxXvaQJMfO/3bCztZE0Z9W0iQYFYI/e8E2UBUd8mPCHBMqj4lUVeoQXumQv6GfSxqejEkS3VksyNDHUPEQ1pLXGx23GWK4AGj2mxJK5/mszmWMMyAtgumEdtE5UX3swpIwMN3fCAycsQ099AhHY3yGsBU6tSPRYuNq7CB0KBLD11pSU6eLxmK6eY7MZw2qHBnfj4aGW1Gu2u17oFwi5tbaZYsok5px1igLDJQVVZRJYWQl829+uyM2lmn/rJu+ux/WVouOH7f5Gk/mg8RLvQHykDG6pqOUbQ3R1Zz4DdolJ4iWKqqAKP3OhvNh07ToKR2aUPwZBC5wmqef4+Qfnw4NV2/knVq9zjRSOifA+xxxSoB7qmtR2hXCPFC/3wY/q6hEbbg8thGaPR46XaAUVhQwRP6xJ1Gc5QcUIatEamDr/brNsafNcqRp6yX7pAL9GETCFTYi3d2+dV2lkf9H5tO9nzAPxt8OWr/CawsEQgZkNIEaUpREJIBroExUdVsezirx/pGOrr6vErv7b4ExaZmIaWMkKVUinxiCiJpXdXVdcdyx+mR7oSnqZ82ZHdX247kGBducBLB/KHcqZCxCKhTRq9TmQsrgLKG8BgWUKI0Vy/i4XvgC28Y+LO3yfUbX/A0dTnvwY6fDAQEE7X8yNehViTiiIQDZSEIEZiWoGyjv7YWlCldBeJ7duQ0IFsh4cU0aRYA7OXnmgL4XUdMK7It/j5NSxemDFgoO/RjjhVEYBhSSBxBAjwm1PqND4vmiw+VgY59pIPl+soNaEjW5fQAlQyVpiaB8QCaJzK9ZLuM7tfre0MGy5tnDd2dg3r0YC0VmJx5z8g+PkYJbfMMMBbB8jcnF84X43a2+Ub6oa9bSg3ZRqkSjs64K9qo7g7d1qs91jVkE7ObqsXkMRN/HX7gxneNGErmlSDCcDg52ztdDBXdXVjHfYi/s8n/Ij6Rg+gypauhBaMkodK5IW9gZhjbOCynQo/B3Hh/S2QjWwBAkWfK94NoZc/1jGQxRnz4YmKYh7VBMBSerVhWyooL/UIKtjKyN6HpqgkRMsBWRWRW5MixHZnvLNowoUroEpZ/SLfIV3YPHlAcIZkuOvuYyn9HRCYkSVeWEA3axJQNFrikADgc/JTUe1262ISVh5+g6dYAyP9/zU8IDWuCVOx/i88dTF/2i6Cdwa/fBTVqE4HI4hnqW4MLttdSog0CMd1ehhFjsNO4023tI6S5gopulpB1IfX4yop26AAwU6iRA2RSEgGCwYK5Bp1gk3uS3qGh5R5W84gqbdFxXv0LAT7gFyJCoZZY0X1W0/8Ug2EsRdC4R4YLKfnME+D+2OGlFXujwX+DYHEGJd0/pmQSPKaumCwblrhuQpsD3MvHh2S8nmeJWjmJDPsaAmLtcnvJOOySfjwvYEJyl+XkvsR6jLjNw8EmQDwC5ODbw/el1Z+JlYLojo1ySpdhZH6CWRySRSC2xnzqopipVz17jSTUb6cuVHuevjmy6J76VYAyCOFFNyDN2kWPSR4BKW8gumhrUoRGdb3SEiqWwxjwlUiohDVavgTAEwaN+daoq5EMQp5603A78I1HOAxdSBIb2gKitCMyNJ4wSiIRSAnrJohWr9ii7NtrcfzX9/0dO7vdKiwHf6/GB+5Tp+OnADTdN+AX6+LfWCLBCuH3IXnDShZOfTJbdAH0heEalf616L/gvQdEDo76TIPV6BizLJf2GewC37867MMEa+mXL+CGx257JzH30X8wOtKFJwQZr86JcudN6UYNf7f4IB45HO7hDTAQeDbdutkKDs1YWKGY3ZHbJF7x1Yc2pbMllgSFuryd8caoP+NsgeBOxIoiAFBfo/mtxc5V7anRN+RwPzA0YuAWYxWWN23ZW8A8IFT3ADJY7yIwcP2bK0kw269azou5rAJpuyViemNihoV+b8u+4JKJrJmRpYO5n7r3ff2V33x2i5YvHFCY/hqulaYRoZI8i6fBnIKvWFLQUuCnKFKwE2oWGGIiB5o+NaBqNthb3awVj96Fd+8TCzcEdfvqLZx9gNtCsuQKb8iDNSXKCPqra020SiXBHAoXMOSGrHBWrs1+/bXgHThkELRHAHher8fNJGcNQIDvlHJLigZA7rw6+PC8C8i4BmXAtbGTzISdllXQTuIKXTyQXIGQtoX/xckVqUGwjR4uVHrxxejVCwP+87bG3jILobGfiJrBKIOQLQCOT0ytRqK1oV97NiwInYU62kWxuazk3pLm7kHshfENpnTRD8a7f5rcLyAAYpgiDQYGYc9+BEHpnbMU1kwKfeEDfR2zMgO42nsB+oD4Yj2i9iL0K9JDLjXoHB2DtNm/mRBC+wb0OKmlDMA0oRrWwWTbZMfDBX0sBo5gaVMP46DITF0H6KV8A5Q3c+SZNkDRSl6pSEIgG0IQcKklehh+MZwk5LQwlBDWe6/0v2pSbGA9AsjRJox83fazzZKcA9hJzXY6+rjEtplLAjEVVTmSVAJuo4psY4XnAXVDIvRCv1p3Q3u5UsFwXimOdLe10rVFCcMhXhM0sSF1GRHwMmQzL7DYMxrs2Utad9lf7idsJKHqr8zoVgGpaAgIKCxpLn+cltfnEAi7YQrCahzfnXYW1sjN7MPjs0gTn/NusgDMsUYCJlHMe7l3vXRP1o8PNvFDCU2YYQQa/MTaI8oTYUqPKcwV+3tnZFEgA9ZZaSyEQswrEbTiK5G3n3fTtQ66e4+c0+hP+0ceIGDgeUqjccAsM5o6Pu00vPJ+F6TJlJM34AC9oTv8BgXa5VOCujr9Pzf2uN9BEdBU6BMvsmUw5BOXDQpIbAcTEJuXMEsh5mnWHKtbfbP5vl5cOoW2kUQWIbBuR3csak+vZ/Yx/bo+NTkvG0VRQLFVDyY8OhhDaoAJjJrjxX6UKCRpnB0hgligRkvJiONIwxoWvmAWI5eFW7E627+nV6JQmlB/twhnRbbM2NkZAvMxkwGJLJCCSspmHWXFfbHLhF+9UyMSAmaSssJ3/xGGjaYZNPWMcSAGVZVwaBdZbgQW6lIpYK6U6Mvs5x1c7Yr6q2OETFppbm1axbfT855I4764g8t/VfPiiroeXShxdGFGDf3o38jp6rBRfaCBndft3mvd9YFkOvUYfWqFNWENnHJ4eNB6Am5G6u/qBbRCuPAQK+J0QohTVJhXELnCT0N3vDSQqLgoht2IHVcLBJaViiclMMO4iCgigZHfps1Tztqfyhi9RQr6K8R0OFI/8vfCExmCAE+8BoFuBKDosSglUtLhCByChCny6elqBSK8pPGuYeQWpsuRhRaGEHg32p1HwSFy2DKJhMfxH1KTcGAIXfF3R0BlG0w8j0mcVvHTQoJledxWZ84BA1wYBSpxetALIMCl13GEktCLhCM/RZgt9XH7N7GVh1/NSEeKLPMD4i+CO3CHpLk3t7FOSpm0A9JEmTJ5877aY8r1tWcITqehOGHMifZUHPZIKElTvonWDo5rFCuquq6zq8e7ulEl6PlQ2RxsTwZgS7V0p9FV7dwCurMXoNVe8sJCfxgJLUyGlN/W84MMdGB/6/jnQ03vvKvyIOhaLml0VNmYinL2862F+nggqQa4sMijZwbfASl33ve0Vxv/gxDI8Tz0etxLl/R7w09N7xd1xczt12C/KCEWlI9njwUtb5/lO43PonFxz+GI2G+HTAMQSyDKQSlLOiTywdCZJe5/97/enJgMrIAfW6SOfYNah3Chx45Ux9/c27KSqV0/m67zKTeW9SiUf1J/Ywm/l86BlTKPmH3pGtoo2hX3KJnhojJY3u+WhYCRgTkd7KyRbLIWjVbQDrFkLehUd9IxgC+lzeGd5AbyjGud72fHchTDGxjG6wkqd9lXFcatIaUhW67HGQv78cjXNi6Fs+/bnQGNelMTRpuAZRhRzIUB1qVBlGWCMIMgwgCkkIggRSQIrIwjFN9SBMTArghJZDBYqxWSOFAjyqHdjQAxtEDjgXkltQyYw8K9kTVZXtSUJ0UFASsQnCOmtdZdp6WPAG0uBKy4cPL7/o/D+sPYAS0gKy7JKNvrzn8/bH5pnRVVnS6yrWPCakWrNCSkTRnp5v5y4+L2vQMwwUDM90I7Seg1laXrO4kZu5OXzk2JqCvKH0EtazESbC5PiuViWDSMJDG0YqKWceFvO+O6Msk9W+z/b8XM2II9n78EXwgiAQ49/KjMG1Bt0W8YCIhmSYbKkSbPxhgcnW1BLVP75tq+JnO92rgqEx4DnJ275vDhwaHI3bbBW3usRNdUauszUlt4IIO68Ehp/5Cz8UWRL40X6mM61hrQqHqEl6/GeNpo28M75qI7CEse6OGnyL/nxj1WzeFCCxfupCRZe2yvnyx5xj67cPqnehDCQuLbIWYY3EuY08HM/H9g6xIFjljBuQOyXmtx7bCnym+kJP1WpA8JlEQWgxi4OzssLe9wKqUgeStqpRAkyChuU05kTpf2QqjZ+jatu7enz0ngCwHULa1bl3s6H9kPp/HmH7NZfyoBSw2kHg4toCaMga4Bz309qqG+Ic4DWHRL66eQCdjuZjxfjZcLVTuKODgeU+/0kUfBzjIAWsF/fjWQGS5mbEJ6oSin6VADrlii8KpDBst6FGMxAF1OEQf36gLhDyaRtR87n2JFhU+lqgUX6DZkKvNFBIaKA8kcMEok+kzb+fTZrk2NPUkiw7Z2ctdKczAY1Q/ns45v6Uc1QEqi9EX/MS/Yt0RK3BBR+etfYD5yoiugE2terThy/3f2UhfzyvuPb+7xywdZ9b0KzBBqWukbplTb3anQ8+HWCMWSXJjoel/bjgEsn2o86JvE+xONjyxNA3XvZ5kNNI9I/NIgpnsajoxarZPhYlb72+5vIttx7edcP41hPVzMjA8zHgKKEgoEx2R5cidFTP9+sC7M/HPnNw49vbS/yQczyrbqoQgltXEe/x591siV5hoeNdiSsEg0gk96LCTeGj2xdaZSXxTWpvxrs6+k0xSgEgAozXsjZ/C1xqxMeGQtbDoKdGcRbYcYOmECkTiO5928UskOaikeaMCnj6G3aL9xZAqwyrH76z6+vtNqBzdbW8YuiLhpSLYFWehyZkXu7KSkpLEWgj0RFiE6NgwtPjGn7aLEDdfjPXo/h+zSwByB/uRCF296qyTYeMmcx8rGibxUy91SyoilTqjSVSiko0VIqVGJRqpQKEBSHJklAYj3TrlFiLnSHuc/LtcQI+3w6wz3Q2CFwbmY0+CwA5m28WsY0NXbYNQzM7GDnA63BItq+A48hBvM4pHV4btajgQNzTuo8FA6gYA+aDALsSE4YRV6u1yyd/R9FD5kffezU5iD01gD5a8vKlUXNWujnDHgyMpjTNFZOLeKEwkNmZpGiFu6B28JmM3Z3urkvOGOS3jFOg35fY3faktdLeR4c/nfh7SUgxCKkqs+2hD/Ffvg9/Zuy8ygJbY6zCsn8FUj8psQ1id1LmHQSroIF8j4eVFfKTyTpPOe7ptk9dxY1a423+TaAXVkhy6kp1bmJxkY93NGzmgnMb+mO/jvyYqwt9IZeylKKQKTm+qwIoo5SYAVOKIgQDAaJB77FIGoAgKMMpP+7nH36aY7eOHrMWmKwZPemTDlZkF49KINDhjIKa6ZuerukkYal81Mm1oQm6Ta3zrL1tMBEUygWi4NvLm6er+5J3X0hnyI68ppJOJ35dNWMs23jY234Twjn782+u/CQket1vN0St9usd8yvF/V043kCwRkYoa9vxgYEdx4RigE5UCUJ8QsWi0IJeUAWJIUMkgUFkWRYhaNVDcGCdH7d/vuERhvQ+SsK7/1KxJEhUXS3BzzoaHhYo0UatIXvVO3Z60OEeIVeB64iBjvmhZ7uqgXIboLGAdf0kXeKQKDRAhMBEAQkl8RXMKTE5xjFsYkmLIUEGyiAaaYzVRoy6LYBNRofg7L9FHEQmGAZQzA7uoI54g5c6tDspZGrFWbSzx8ezZYS6BHilDBIiCmLPIC97yn0dG7LuuKgdcyQv9cJRJBTIT2+BVBlq52e0l2EZkLHNpLDBQG4RlttbRhf01VwKZBIepzRTogGpkb2EqQWO2igNFMhqB3QOECvfaBW1ykc+viX9VUUhBIThggCbAUQoS1yZQGFDURSVoncE+Ovp1a9iFEM7zs07hb+yt4E5I6qaejLW5OzdU8+zeTbUEzB9DV46pDkHWhQBPVjI55gQOboPJwx6gRiogxJ0b79HHz37t/U17nlr6nr/YxEshgdkx2dPIxtY7jxyViMyEW0FhYPqkDQke/mkG9BPNA89c85b4CJJRBYZ2c982ODjkAeKFwK6qnAmlNCe/WwT3gqwvkkZ3u8MGkeluaOgMaWFVjvpR//F3JFOFCQuOFHqw==')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
